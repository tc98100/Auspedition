# Generated by Django 2.2.5 on 2020-11-15 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20201115_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='bookmark',
        ),
        migrations.RemoveField(
            model_name='attraction',
            name='userLike',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='bookmark',
        ),
        migrations.RemoveField(
            model_name='destination',
            name='userLike',
        ),
    ]
