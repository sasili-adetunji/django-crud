
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserProfile = get_user_model()

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User Profile objects
    """
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'username', 'password')

        read_only_fields = (
            'created_on',
        )

        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'username': {'required': True},
            'email': {'required': True},
        }

    def create(self, validated_data):
        """
        Create and return a new user
        :param validated_data:
        :return:
        """
        user = UserProfile(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user