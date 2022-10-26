
from django.contrib import admin
from django.urls import path, include

import examPrep2

urlpatterns = [
    path('', include('examPrep2.my_music_app.urls')),
    path('admin/', admin.site.urls),
]
