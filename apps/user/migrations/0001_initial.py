# Generated by Django 4.1.7 on 2023-03-31 20:50

import apps.user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_activate', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('verificated', models.BooleanField(default=False)),
                ('requested_instructor', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, default='users/user_default_profile.png', upload_to=apps.user.models.user_profile_directory_path)),
                ('banner', models.ImageField(blank=True, default='users/user_default_bg.jpg', upload_to=apps.user.models.user_banner_directory_path)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('profile_info', models.TextField(blank=True, max_length=150, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
