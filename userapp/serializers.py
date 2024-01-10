from django.db import transaction
from rest_framework import serializers

from userapp.models import App


class AdminUserappSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'title', 'description', 'owner', 'is_verified', 'cost')
        read_only_fields = ('id', )


class UserappSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'title', 'description', 'owner', 'is_verified', 'cost')
        read_only_fields = ('is_verified', 'id', )


class VerifiedAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'title', 'description', 'owner', 'is_verified', 'cost')


class PurchaseAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'title', 'description', 'owner', 'is_verified', 'cost')

    @transaction.atomic
    def update(self, instance, validated_data):
        buyer = self.context['request'].user
        if buyer.credit < instance.cost:
            return

        buyer.credit -= instance.cost
        buyer.save()

        instance.owner.credit += instance.cost
        instance.owner.save()

        return instance
