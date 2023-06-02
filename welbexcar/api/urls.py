from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CarViewSet, CargoViewSet

app_name = 'api'

router = DefaultRouter()
router.register('cars', CarViewSet, 'cars')
router.register('cargo', CargoViewSet, 'cargo')


urlpatterns = [
    path('', include(router.urls)),
]
