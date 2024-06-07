from django.db import models

class RoomImage(models.Model):
    image_url = models.ImageField(upload_to='room_images/')
    # other fields...

# other models...
