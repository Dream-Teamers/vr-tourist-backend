# Generated by Django 4.1.13 on 2024-06-09 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='locations',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='price',
            new_name='price_per_night',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='price',
            new_name='price_per_night',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='hotel_url',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='room',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_url',
        ),
        migrations.RemoveField(
            model_name='room',
            name='tags',
        ),
        migrations.AddField(
            model_name='hotel',
            name='amenities',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='rooms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.room'),
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.room')),
            ],
        ),
    ]
