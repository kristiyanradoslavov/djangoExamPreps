from django.urls import path, include
from CarCollection.car.views import car_edit, car_create, car_delete, car_details

urlpatterns = [
    path('create/', car_create, name='create car'),
    path('<int:car_id>/', include([
        path('details/', car_details, name='car details'),
        path('edit/', car_edit, name='edit car'),
        path('delete/', car_delete, name='delete car'),
    ])),
]
