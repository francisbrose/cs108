# Generated by Django 3.0.5 on 2020-04-13 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_fb', '0004_profile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bday',
            field=models.TextField(blank=True),
        ),
    ]
