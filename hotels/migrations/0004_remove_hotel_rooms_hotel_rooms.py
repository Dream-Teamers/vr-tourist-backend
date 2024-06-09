# Generated by Django 4.1.13 on 2024-06-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_remove_room_created_remove_room_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='rooms',
        ),
        migrations.AddField(
            model_name='hotel',
            name='rooms',
            field=models.ManyToManyField(blank=True, related_name='rooms', to='hotels.room'),
        ),
    ]