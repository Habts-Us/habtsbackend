# Generated by Django 3.2.23 on 2023-12-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_customuser_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='expo_token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
