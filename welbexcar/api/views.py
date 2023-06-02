from django.shortcuts import render
from cargo.models import Car, Cargo
from api.serializers import CarSerializer, CargoListSerializer, CargoDetailSerializer
from rest_framework import viewsets


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    http_method_names = ['get', 'patch']


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.select_related(
        'pick_up_location',
        'delivery_location'
    )

    serializer_class = CargoDetailSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.action == 'list':
            return CargoListSerializer
        elif self.action == 'retrieve':
            return CargoDetailSerializer
        return super().get_serializer_class()
