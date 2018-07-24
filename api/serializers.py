
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User Profile objects
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'name')

        read_only_fields = (
            'created_on',
        )

        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
        }

    def create(self, validated_data):
        """
        Create and return a new user
        :param validated_data:
        :return:
        """
        user = User(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.save()

        return user
