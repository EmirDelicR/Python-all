# Generated by Django 2.1.4 on 2018-12-07 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_completed',
            field=models.BooleanField(default=False),
        ),
    ]