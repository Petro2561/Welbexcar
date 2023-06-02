from rest_framework import serializers
from cargo.models import Car, Cargo, Location
from geopy.distance import geodesic as GD


class CargoListSerializer(serializers.ModelSerializer):
    pick_up_location = serializers.SlugRelatedField(
        slug_field='zip',
        queryset=Location.objects.all()
    )
    delivery_location = serializers.SlugRelatedField(
        slug_field='zip',
        queryset=Location.objects.all()
    )
    quantity_of_nearby_cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = '__all__'

    def get_quantity_of_nearby_cars(self, obj):
        """Функция возвращает количество машин,
        подходящих по весу и находящихся не дальше 450 миль"""
        cars = Car.objects.annotate().filter(load_capacity__gte=obj.weight)
        pick_up = (obj.pick_up_location.lat, obj.pick_up_location.lng)
        quantity_of_nearby_car = [
            car.car_number for car in cars
            if GD(pick_up, (car.current_location.lat,
                            car.current_location.lng)).mi <= 450
        ]
        return len(quantity_of_nearby_car)


class CargoDetailSerializer(serializers.ModelSerializer):
    pick_up_location = serializers.SlugRelatedField(
        slug_field='zip',
        queryset=Location.objects.all()
    )
    delivery_location = serializers.SlugRelatedField(
        slug_field='zip',
        queryset=Location.objects.all()
    )
    nearby_cars = serializers.SerializerMethodField()

    class Meta:
        model = Cargo
        fields = '__all__'

    def get_nearby_cars(self, obj):
        """Функция возвращает номера всех машин
        и расстояние до них в мидях"""
        pick_up = (obj.pick_up_location.lat, obj.pick_up_location.lng)
        cars = Car.objects.filter(load_capacity__gte=obj.weight)
        nearby_car = [
            (car.car_number, GD(pick_up, ((car.current_location.lat),
            (car.current_location.lng))).mi)  for car in cars
        ]
        return nearby_car

    def update(self, instance, validated_data):
        # Обновление веса и описания для груза
        instance.weight = validated_data.get('weight', instance.weight)
        instance.description = validated_data.get(
            'description', instance.description
        )
        instance.save()
        return instance


class CarSerializer(serializers.ModelSerializer):
    current_location = serializers.SlugRelatedField(
        slug_field='zip',
        queryset=Location.objects.all()
    )

    class Meta:
        model = Car
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.current_location = validated_data.get('current_location', instance.current_location)
        instance.save()
        return instance
