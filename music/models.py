from django.db import models
from django.core.urlresolvers import reverse

#variables(attributes) declared here will automatically be converted into columns in the database by django,and classes as tables
#django automatically creates a default column 'id'
#red pk 1..no two albums have same id
class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    #album_logo = models.CharField(max_length=1000)
    album_logo = models.FileField() #this will work for admin

    def get_absolute_url(self): #details page of album we just created
        return reverse('music:detail', kwargs={'pk':self.pk})
    def __str__(self):      #__ means string representation of object...detailed explanation
        return self.album_title + ' - ' + self.artist



#foreign key will be 1
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)  #when album red is deleted, delete songs linked to it
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_fav = models.BooleanField(default=False)
    def __str__(self):  # __ means string representation of object...detailed explanation
        return self.song_title