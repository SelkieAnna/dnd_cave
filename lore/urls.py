from django.urls import path, include
from . import views
from rest_framework import routers
from lore import views
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'characters', views.CharacterViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'factions', views.FactionViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'places', views.PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]