from django.contrib import admin
from django.db import models

from examPrep2.my_music_app.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass
