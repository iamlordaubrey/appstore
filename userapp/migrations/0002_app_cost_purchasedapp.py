# Generated by Django 5.0.1 on 2024-01-09 20:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='PurchasedApp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userapp.app')),
            ],
        ),
    ]