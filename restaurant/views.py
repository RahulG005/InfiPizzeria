from django.shortcuts import render
from .models import Menu, Booking
from rest_framework import generics, viewsets
from .serializers import Menuserializer, Bookingserializer


# Create your views here.
def index(request):
    return render(request, 'index.html')

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer

class Bookingview(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = Bookingserializer