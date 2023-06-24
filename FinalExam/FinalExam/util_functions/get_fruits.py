from FinalExam.fruits.models import Fruit


def get_all_fruits():
    fruit = Fruit.objects.all()

    return fruit


def get_fruit(fruit_id):
    fruit = Fruit.objects.filter(id=fruit_id).get()

    return fruit
