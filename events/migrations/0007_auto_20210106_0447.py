# Generated by Django 3.1.4 on 2021-01-06 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20210106_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
