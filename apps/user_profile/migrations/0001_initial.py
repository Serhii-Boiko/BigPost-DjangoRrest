# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 21:01
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='email')),
                ('about', models.TextField(blank=True, null=True, validators=[django.core.validators.MaxLengthValidator(2000)], verbose_name='about')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user profile',
                'verbose_name_plural': 'users profiles',
                'ordering': ['pk'],
            },
        ),
    ]
