# Generated by Django 3.2.23 on 2023-12-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_customuser_lang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='is_premium',
        ),
        migrations.AddField(
            model_name='customuser',
            name='premium',
            field=models.BooleanField(default=False),
        ),
    ]
