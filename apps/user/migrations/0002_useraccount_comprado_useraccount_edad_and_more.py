# Generated by Django 4.1.7 on 2023-05-18 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='comprado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='pais',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='salario',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]