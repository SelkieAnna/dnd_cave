from django.db import models

class Place(models.Model):
    name            = models.CharField(max_length=30)
    mood_media_link = models.CharField(max_length=2048, blank=True)
    description     = models.TextField(blank=True)

    characters = models.ManyToManyField('lore.Character')
    events = models.ManyToManyField('lore.Event')
    factions = models.ManyToManyField('lore.Faction')
    places = models.ManyToManyField('lore.Place')

    # look = (picture, a set of unique fetures)
    # sounds = (a set of sounds that the players might hear on this location)
    # feel = (a set of unique feels that the player might get)
    # characters = (characters that are linked to this location)
    # quests = (quests on this location)
    