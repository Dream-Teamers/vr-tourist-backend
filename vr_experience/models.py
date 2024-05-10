from django.db import models
import uuid

class VRExperience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    locations = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    _id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title
    
class VRReview(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    rating = models.CharField(max_length=200, choices=VOTE_TYPE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    vr_experience = models.ForeignKey(VRExperience, on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    _id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.rating
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    _id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.name