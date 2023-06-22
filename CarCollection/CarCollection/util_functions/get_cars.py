from CarCollection.car.models import Car


def get_cars(*car_id):
    if car_id:
        cars = Car.objects.filter(pk=car_id[0]).get()
    else:
        cars = Car.objects.all()

    return cars
