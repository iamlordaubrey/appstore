from rest_framework import serializers

from userapp.models import App


class AdminUserappSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'title', 'description', 'is_verified')


class UserappSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'title', 'description', 'is_verified')
        read_only_fields = ('is_verified',)
