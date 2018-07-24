
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
        fields = ('id', 'email', 'name')

        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True }
        }

    def create(self, validated_data):
        """
        Create and return a new user
        :param validated_data:
        :return:
        """
        user = UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.save()

        return user