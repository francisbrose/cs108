# Generated by Django 3.0.4 on 2020-04-28 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_remove_specimen_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='individual',
            name='lab',
        ),
    ]
