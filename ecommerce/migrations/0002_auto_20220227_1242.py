# Generated by Django 3.1 on 2022-02-27 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='bannerbottom1',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='bannerbottom2',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='bannerlast1',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='bannerlast2',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='contactbanner',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='schedulebottom',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='trending1',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='trending2',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='trending3',
        ),
    ]
