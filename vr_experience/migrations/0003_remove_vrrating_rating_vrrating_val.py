# Generated by Django 4.1.13 on 2024-05-20 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vr_experience', '0002_remove_vrrating_vr_experience_vrexperience_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vrrating',
            name='rating',
        ),
        migrations.AddField(
            model_name='vrrating',
            name='val',
            field=models.CharField(blank=True, choices=[('5', 5), ('4', 4), ('3', 3), ('2', 2), ('1', 1)], max_length=200, null=True),
        ),
    ]
