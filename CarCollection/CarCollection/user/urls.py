from django.urls import path, include
from CarCollection.user.views import user_details, user_edit, user_create, user_delete

urlpatterns = [
    path('create/', user_create, name='create user'),
    path('details/', user_details, name='user details'),
    path('edit/', user_edit, name='user edit'),
    path('delete/', user_delete, name='user delete'),
]
