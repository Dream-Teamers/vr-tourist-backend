from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=255)
    locations = models.CharField(max_length=255)
    image_url = models.URLField()
    tour_url = models.URLField()

    def __str__(self):
        return self.title

class TourAgency(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    tours = models.ManyToManyField(Tour, related_name='agencies')

    def __str__(self):
        return self.name

class AgencyRating(models.Model):
    agency = models.ForeignKey(TourAgency, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'Rating {self.rating} for {self.agency.name} by {self.user.username}'

class TourBooking(models.Model):
    tour = models.ForeignKey(Tour, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_people = models.IntegerField()

    def __str__(self):
        return f'Booking for {self.tour.title} by {self.user.username}'
