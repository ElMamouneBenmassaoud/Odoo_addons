# Generated by Django 4.2.1 on 2023-10-09 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': [('task_management', 'Can create, assign and delete tasks')]},
        ),
    ]
