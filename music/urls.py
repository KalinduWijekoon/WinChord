from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    # url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    # /music/<album no(712)>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    # /music/album/add/
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    # /music/album/2/
    #url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='album-delete'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),

]
