# Generated by Django 4.1 on 2022-09-07 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bulletinboard',
            name='updated_at',
        ),
    ]
