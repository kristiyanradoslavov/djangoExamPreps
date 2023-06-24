from django.urls import path

from FinalExam.fruits.views import fruit_create, fruit_details, fruit_edit, fruit_delete

urlpatterns = [
    path('', fruit_create, name='create fruit'),
    path('details/', fruit_details, name='fruit details'),
    path('edit/', fruit_edit, name='edit fruit'),
    path('delete/', fruit_delete, name='delete fruit'),
]
