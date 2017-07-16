#^ is used to start and $ is used to end the text by user
# $ without any text preceding means default homepage of music
from django.conf.urls import url
from . import views     #dot means look for views in the same directory

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),  #access index function in views.py
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /music/71[this is album_id]/
    #url(r'^(?P<album_id>[0-9]+)/$',views.DetailView.as_view(),name = "detail"),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name = "detail"),
    # /music/71/fav/[this is album_id]/
    #url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name = "favourite"),

    #/music/album/add...no need of primary key expression coz we r adding a new album
    url(r'album/add/$',views.AlbumCreate.as_view(),name='album-add'),

    #/music/album/pk/ for update
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

    #/music/album/pk/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

]
