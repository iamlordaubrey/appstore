import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class App(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)


class PurchasedApp(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    key = models.UUIDField(unique=True, default=uuid.uuid4)
    app = models.ForeignKey(App, null=True, on_delete=models.SET_NULL)
