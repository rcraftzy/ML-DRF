from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'id',
            'account',
            'username',
            'email',
            'first_name',
            'last_name',
            'is_activate',
            'is_staff',
            'verificated',
            'requested_instructor',
            'picture',
            'banner',
            'location',
            'url',
            'birthday',
            'profile_info',
            'date_created',
            'pais',
            'edad',
            'salario',
            'comprado',
        ]
