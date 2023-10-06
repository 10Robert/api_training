# Generated by Django 4.2.5 on 2023-10-06 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_users_data_create_users_data_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='hours_create',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='users',
            name='hours_modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
