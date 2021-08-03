from django.db import models

class Faction(models.Model):
    name        = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    
    characters = models.ManyToManyField('lore.Character')
    events = models.ManyToManyField('lore.Event')
    factions = models.ManyToManyField('lore.Faction')
    items = models.ManyToManyField('lore.Item')
    places = models.ManyToManyField('lore.Place')

    owner = models.ForeignKey('auth.User', related_name='faction_owner', on_delete=models.CASCADE)
