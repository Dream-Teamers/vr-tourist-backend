# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# # from .forms import VRForm, RatingForm
# from .models import Hotel, Room, RoomReview, RoomBooking
# from django.contrib.auth.decorators import login_required
# def hotelsPage(request):
#     hotels = Hotel.objects.all()
#     message = "Hotels"
#     context = {
#         'hotels': hotels,
#         'message': message,
#         'rating_range': list(range(1,6)),

#     }
#     return render(request, 'hotels/hotels.html', context)
# def hotelPage(request,pk):
#     hotel = Hotel.objects.get(name=pk)
#     message = "Hotel"
#     context = {
#         'hotel': hotel,
#         'message': message,
#         'rating_range': list(range(1,6)),

#     }
#     return render(request, 'hotels/single-hotel.html', context)

# @login_required(login_url='login')
# def hotel_manager_dashboard(request):
#     return render(request, 'hotels/hotel_manager_dashboard.html')



# @login_required(login_url='login')
# def add_hotel_listing(request):
#     # Implement functionality to add hotel listing
#     return render(request, 'hotel/add_hotel_listing.html')

# @login_required(login_url='login')
# def update_hotel_listing(request):
#     # Implement functionality to update hotel listing
#     return render(request, 'hotel/update_hotel_listing.html')

# @login_required(login_url='login')
# def delete_hotel_listing(request):
#     # Implement functionality to delete hotel listing
#     return render(request, 'hotel/delete_hotel_listing.html')

# @login_required(login_url='login')
# def view_hotel_bookings(request):
#     # Implement functionality to view hotel bookings
#     return render(request, 'hotel/view_hotel_bookings.html')

# @login_required(login_url='login')
# def manage_hotel_reviews(request):
#     # Implement functionality to manage hotel reviews
#     return render(request, 'hotel/manage_hotel_reviews.html')


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, RoomBooking, Hotel, Tag, HotelRating
from django.utils.dateparse import parse_date

# Hotel Management
def hotelsPage(request):
    hotels = Hotel.objects.all()
    message = "Hotels"
    context = {
        'hotels': hotels,
        'message': message,
        'rating_range': list(range(1, 6)),
    }
    return render(request, 'hotels/hotels.html', context)

def hotelPage(request, pk):
    hotel = get_object_or_404(Hotel, name=pk)
    if request.method == "POST":
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        HotelRating.objects.create(
            user=request.user,
            hotel=hotel,
            rating=rating,
            comment=comment
        )
        messages.success(request, 'Rating submitted successfully')
        return redirect('single-hotel', pk=pk)

    context = {
        'hotel': hotel,
        'rating_range': list(range(1, 6)),
    }
    return render(request, 'hotels/single-hotel.html', context)

@login_required(login_url='login')
def hotel_manager_dashboard(request):
    return render(request, 'hotels/hotel_manager_dashboard.html')

@login_required(login_url='login')
def add_hotel_listing(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        locations = request.POST.get('locations')
        image_url = request.POST.get('image_url')
        image = request.FILES.get('image')
        tag_ids = request.POST.getlist('tags')

        hotel = Hotel.objects.create(
            name=name,
            description=description,
            locations=locations,
            image_url=image_url,
            image=image,
        )

        if tag_ids:
            tags = Tag.objects.filter(id__in=tag_ids)
            hotel.tags.set(tags)
        messages.success(request, 'Hotel listing added successfully')
        return redirect('hotels')

    tags = Tag.objects.all()
    return render(request, 'hotels/add_hotel_listing.html', {'tags': tags})

@login_required(login_url='login')
def update_hotel_listing(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == "POST":
        hotel.name = request.POST.get('name')
        hotel.description = request.POST.get('description')
        hotel.locations = request.POST.get('locations')
        hotel.image_url = request.POST.get('image_url')
        hotel.save()

        hotel.tags.clear()
        tags = request.POST.getlist('tags')
        for tag_id in tags:
            tag = get_object_or_404(Tag, pk=tag_id)
            hotel.tags.add(tag)

        messages.success(request, 'Hotel listing updated successfully')
        return redirect('hotels')

    tags = Tag.objects.all()
    context = {
        'hotel': hotel,
        'tags': tags,
    }
    return render(request, 'hotels/update_hotel_listing.html', context)

@login_required(login_url='login')
@login_required(login_url='login')
def delete_hotel_listing(request, pk):
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        messages.success(request, 'Hotel deleted successfully')
        return redirect('hotels')
    context = {'hotel': hotel}
    return render(request, 'hotels/delete_hotel_listing.html', context)

@login_required(login_url='login')
def view_hotel_bookings(request):
    bookings = RoomBooking.objects.filter(user=request.user)
    context = {
        'bookings': bookings
    }
    return render(request, 'hotels/view_hotel_bookings.html', context)

@login_required(login_url='login')
def manage_hotel_reviews(request):
    reviews = HotelRating.objects.filter(user=request.user)
    context = {
        'reviews': reviews
    }
    return render(request, 'hotels/manage_hotel_reviews.html', context)

# Room Management
@login_required(login_url='login')
def room_list(request, hotel_id):
    rooms = Room.objects.all()
    return render(request, 'rooms/room_list.html', {'rooms': rooms})

@login_required(login_url='login')
def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'rooms/room_detail.html', {'room': room})



@login_required(login_url='login')
def room_add(request, pk):
    if request.method == 'POST':
        hotel_id = pk
        room_type = request.POST.get('room_type')
        occupancy = request.POST.get('occupancy')
        price_per_night = request.POST.get('price_per_night')
        total_rooms = request.POST.get('total_rooms')
        if total_rooms is not None:  # Check if 'total_rooms' is not None
            total_rooms = int(total_rooms)  # Convert to int
        else:
            total_rooms = 0  # Default to 0 if 'total_rooms' is None
        available_rooms = total_rooms  # Initially, all rooms are available

        if occupancy is not None:  # Check if 'occupancy' is not None
            occupancy = int(occupancy)  # Convert to int
        else:
            occupancy = 0  # Default to 0 if 'occupancy' is None

        hotel = get_object_or_404(Hotel, pk=pk)
        Room.objects.create(hotel=hotel, room_type=room_type, occupancy=occupancy,
                            price_per_night=price_per_night, total_rooms=total_rooms, available_rooms=available_rooms)
        messages.success(request, 'Room created successfully')
        return redirect('room_list')

    hotels = Hotel.objects.all()
    return render(request, 'hotels/room_form.html', {'hotels': hotels})



@login_required(login_url='login')
def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.room_type = request.POST.get('room_type')
        room.occupancy = request.POST.get('occupancy')
        room.price_per_night = request.POST.get('price_per_night')
        total_rooms = request.POST.get('total_rooms')
        room.total_rooms = total_rooms
        room.available_rooms = total_rooms - (room.total_rooms - room.available_rooms)  # Adjust available rooms
        room.save()
        messages.success(request, 'Room updated successfully')
        return redirect('room_list')
    hotels = Hotel.objects.all()
    return render(request, 'rooms/room_form.html', {'room': room, 'hotels': hotels})

@login_required(login_url='login')
def deleteRoom(request, pk):
    room = get_object_or_404(Room, name=pk)
    if request.method == 'POST':
        room.delete()
        messages.success(request, 'Room deleted successfully')
        return redirect('room_list')
    return render(request, 'hotels/vrs.html', {'room': room})


def room_list(request, hotel_id):
    rooms = Room.objects.filter(hotel_id=hotel_id)
    return render(request, 'rooms.html', {'rooms': rooms})




@login_required(login_url='login')
def check_room_availability(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        num_rooms = int(request.POST.get('num_rooms'))
        if room.available_rooms >= num_rooms:
            room.available_rooms -= num_rooms
            room.save()
            total_price = num_rooms * room.price_per_night
            RoomBooking.objects.create(
                room=room,
                user=request.user,
                check_in_date=parse_date(request.POST.get('check_in_date')),
                check_out_date=parse_date(request.POST.get('check_out_date')),
                total_price=total_price
            )
            messages.success(request, 'Room(s) booked successfully')
            return redirect('room_list')
        else:
            messages.error(request, 'Not enough available rooms for the selected quantity')
    return render(request, 'rooms/check_availability.html', {'room': room})
