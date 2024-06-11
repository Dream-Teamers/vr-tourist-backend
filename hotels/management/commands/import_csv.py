# myapp/management/commands/import_csv.py
import csv
from django.core.management.base import BaseCommand
from hotels.models import Hotel, Room, RoomImage,HotelRating
# from agencies.models import TourAgency, Tour, TourBooking
from django.contrib.auth.models import User
from datetime import datetime
class Command(BaseCommand):
    help = 'Load CSV data into the database'

    def handle(self, *args, **kwargs):
        # self.import_tour_agency()
        # self.import_tour()
        self.import_hotel()
        # # self.import_room()
        # self.import_room_image()
        # # self.import_tour_booking()
        # self.import_hotel_rating()
    def import_hotel(self):
        admin_user = User.objects.get(id=2)

        hotels = [
            {
                "name": "Entoto Hotel",
                "address": "Entoto Street, Addis Ababa",
                "description": "A luxurious stay at the foot of Entoto Hill",
                "rating": 4.5,
                "amenities": "Free WiFi, Pool, Spa",
                "price_per_night": 150.00,
                "image_url": "http://example.com/entoto_hotel.jpg",
                "created": datetime.now()
            },
            {
                "name": "National Palace Hotel",
                "address": "4 Killo, Addis Ababa",
                "description": "Stay next to the National Palace",
                "rating": 4.0,
                "amenities": "Free Breakfast, Gym, Sauna",
                "price_per_night": 200.00,
                "image_url": "http://example.com/national_palace_hotel.jpg",
                "created": datetime.now()
            },
            {
                "name": "Lalibela Lodge",
                "address": "Lalibela Town, Lalibela",
                "description": "Comfort and convenience in Lalibela",
                "rating": 3.5,
                "amenities": "Free Parking, Restaurant",
                "price_per_night": 100.00,
                "image_url": "http://example.com/lalibela_lodge.jpg",
                "created": datetime.now()
            },
            {
                "name": "Axum Grand Hotel",
                "address": "Axum Main Road, Axum",
                "description": "Luxurious stay with a view of ancient obelisks",
                "rating": 4.2,
                "amenities": "Free WiFi, Pool, Historical Tours",
                "price_per_night": 180.00,
                "image_url": "http://example.com/axum_grand_hotel.jpg",
                "created": datetime.now()
            },
            {
                "name": "Gondar Castle Hotel",
                "address": "Castle Road, Gondar",
                "description": "Experience the history of Gondar from your hotel",
                "rating": 4.0,
                "amenities": "Free Breakfast, Castle Tours, Pool",
                "price_per_night": 160.00,
                "image_url": "http://example.com/gondar_castle_hotel.jpg",
                "created": datetime.now()
            },
            {
                "name": "Simien Mountains Lodge",
                "address": "Simien Mountains, Ethiopia",
                "description": "Stay in the heart of the Simien Mountains National Park",
                "rating": 4.8,
                "amenities": "Guided Hikes, Wildlife Viewing, Free Breakfast",
                "price_per_night": 250.00,
                "image_url": "http://example.com/simien_mountains_lodge.jpg",
                "created": datetime.now()
            },
            {
                "name": "Bahir Dar Blue Nile Resort",
                "address": "Blue Nile Avenue, Bahir Dar",
                "description": "Luxury resort on the shores of Lake Tana",
                "rating": 4.5,
                "amenities": "Boat Tours, Free WiFi, Pool",
                "price_per_night": 220.00,
                "image_url": "http://example.com/bahir_dar_resort.jpg",
                "created": datetime.now()
            },
            {
                "name": "Harar Jugol Hotel",
                "address": "Old Town, Harar",
                "description": "Stay in the historic walled city of Harar",
                "rating": 3.8,
                "amenities": "Free Breakfast, Historical Tours, Cultural Shows",
                "price_per_night": 140.00,
                "image_url": "http://example.com/harar_jugol_hotel.jpg",
                "created": datetime.now()
            },
            {
                "name": "Dire Dawa International Hotel",
                "address": "Main Street, Dire Dawa",
                "description": "Modern comforts in the heart of Dire Dawa",
                "rating": 4.0,
                "amenities": "Free WiFi, Gym, Pool",
                "price_per_night": 170.00,
                "image_url": "http://example.com/dire_dawa_hotel.jpg",
                "created": datetime.now()
            },
            {
                "name": "Awash Falls Lodge",
                "address": "Awash National Park, Awash",
                "description": "Eco-friendly lodge near the Awash Falls",
                "rating": 4.5,
                "amenities": "Guided Tours, Wildlife Viewing, Free Breakfast",
                "price_per_night": 200.00,
                "image_url": "http://example.com/awash_falls_lodge.jpg",
                "created": datetime.now()
            }
        ]

        for hotel_data in hotels:
            Hotel.objects.create(
                admin=admin_user,
                name=hotel_data["name"],
                address=hotel_data["address"],
                description=hotel_data["description"],
                rating=hotel_data["rating"],
                amenities=hotel_data["amenities"],
                price_per_night=hotel_data["price_per_night"],
                image_url=hotel_data["image_url"],
                created=hotel_data["created"]
            )

    print("10 hotels have been added successfully.")

    
