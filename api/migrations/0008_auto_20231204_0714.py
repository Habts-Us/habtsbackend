# Generated by Django 3.2.23 on 2023-12-04 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20231128_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('progress', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('frequency', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=20)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reminder_time', models.TimeField(blank=True, null=True)),
                ('specific_days_of_week', models.CharField(blank=True, max_length=20, null=True)),
                ('specific_day_of_month', models.PositiveIntegerField(blank=True, null=True)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='diaryentry',
            name='team',
        ),
        migrations.RemoveField(
            model_name='moodtracker',
            name='team',
        ),
        migrations.RemoveField(
            model_name='moodtracker',
            name='user',
        ),
        migrations.AlterField(
            model_name='collaborativelist',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='BillingInfo',
        ),
        migrations.DeleteModel(
            name='DiaryEntry',
        ),
        migrations.DeleteModel(
            name='MoodTracker',
        ),
        migrations.AddField(
            model_name='dailyprogress',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.habit'),
        ),
        migrations.AddField(
            model_name='dailyprogress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
