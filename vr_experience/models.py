from django.db import models
import uuid
from django.contrib.auth.models import User


class VRExperience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    deleted = models.BooleanField(default=False, editable=False)
    tags = models.ManyToManyField('Tag', blank=True)
    # rating = models.IntegerField(default=5)
    locations = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    
class VRRating(models.Model):
    VOTE_TYPE = (
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vr_experience = models.ForeignKey(VRExperience, on_delete=models.CASCADE)
    value = models.CharField(max_length=200, choices=VOTE_TYPE, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.value}"
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self) -> str:
    #     return self.name
    
class VRBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vr_experience = models.ForeignKey(VRExperience, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
