
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from account.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    # password = forms.CharField()
    # password2 = forms.CharField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email', 
            'first_name', 
            'last_name',
            'address',
            'city',
            'postal_code',
            'about'
        ]
        


    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            # if settings.SEND_ACTIVATION_EMAIL:
            #     user.is_active = False
            #     user.save(update_fields=["is_active"])
        return user
        