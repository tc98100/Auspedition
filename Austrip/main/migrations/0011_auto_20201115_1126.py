# Generated by Django 2.2.5 on 2020-11-15 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20201115_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normaluser',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='email',
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
