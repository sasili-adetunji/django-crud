from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Helps django work with our custom user model"""

    def create_user(self, email, username, name, password=None):
        """ Create a new user profile """

        if not email:
            raise ValueError("Users must have an email address")
        
        if not password:
            raise ValueError("User must have a password")
        
        if not username:
            raise ValueError("User must have a full name")
        
        email = self.normalize_email(email)

        user = self.model(email=email, username=username)
      
        user.name = name
        
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, username, password):
        """ Create and save a new superuser with given details """

        user = self.create_user(email, username, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents a user profile in our application """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name', 'username']

    def get_full_name(self):
        """ Used to get a user's full name """

        return self.name

    def get_short_name(self):
        """ Used to get a user's short name """

        return self.name

    def __str__(self):
        """ Django uses this when it needs to converts the object to string """

        return self.email
