from django.db import models

class Event(models.Model):
    name        = models.CharField(max_length=30)
    description = models.TextField(blank=True)

    characters = models.ManyToManyField('lore.Character')
    factions = models.ManyToManyField('lore.Faction')
    places = models.ManyToManyField('lore.Place')
