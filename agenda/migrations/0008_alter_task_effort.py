# Generated by Django 4.1.6 on 2023-02-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_alter_task_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='effort',
            field=models.CharField(choices=[('Myself', 'Myself'), ('Other', 'Other'), ('Task', 'Task')], default=False, max_length=150),
        ),
    ]
