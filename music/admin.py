from django.contrib import admin
from .models import Album,Song
#giving class Album an admin interface
admin.site.register(Album)
admin.site.register(Song)
