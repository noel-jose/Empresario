# Generated by Django 3.1.4 on 2021-01-04 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_reg_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='desc',
            new_name='description',
        ),
    ]
