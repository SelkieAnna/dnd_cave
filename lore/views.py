from .models import *       #TODO: rewrite import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CharacterSerializer, EventSerializer, FactionSerializer, ItemSerializer, PlaceSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = [permissions.IsAuthenticated]

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_class = [permissions.IsAuthenticated]

class FactionViewSet(viewsets.ModelViewSet):
    queryset = Faction.objects.all()
    serializer_class = FactionSerializer
    permission_class = [permissions.IsAuthenticated]

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_class = [permissions.IsAuthenticated]

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_class = [permissions.IsAuthenticated]
