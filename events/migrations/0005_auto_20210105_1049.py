# Generated by Django 3.1.4 on 2021-01-05 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210105_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_start_date',
            field=models.DateTimeField(),
        ),
    ]
