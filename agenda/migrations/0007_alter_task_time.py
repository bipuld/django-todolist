# Generated by Django 4.1.6 on 2023-02-11 04:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_task_effort_alter_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
