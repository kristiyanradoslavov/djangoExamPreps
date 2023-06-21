from django.urls import path, include
from CarCollection.common.views import catalogue, index

urlpatterns = [
    path('', index, name='index'),
    path('catalogue/', catalogue, name='catalogue')
]
