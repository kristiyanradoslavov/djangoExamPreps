from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicAppProject.common.urls')),
    path('album/', include('musicAppProject.album.urls')),
    path('profile/', include('musicAppProject.account.urls')),

]
