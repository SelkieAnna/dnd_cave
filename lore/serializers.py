from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['name', 'id']
        read_only_fields = ('owner',)


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name', 'id']
        read_only_fields = ('owner',)


class FactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faction
        fields = ['name', 'id']
        read_only_fields = ('owner',)


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'id']
        read_only_fields = ('owner',)


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Place
        fields = ['name', 'id', 'mood_media_link', 'description']
        read_only_fields = ('owner',)


class UserSerializer(serializers.ModelSerializer):
    characters = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Character.objects.all()
    )
    events = serializers.PrimaryKeyRelatedField(many=True, queryset=Event.objects.all())
    factions = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Faction.objects.all()
    )
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    places = serializers.PrimaryKeyRelatedField(many=True, queryset=Place.objects.all())

    class Meta:
        model = User
        fields = ["id", "username"]
