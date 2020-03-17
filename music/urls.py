from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    # /music/
    # url(r'^admin/', admin.site.urls),
    path('', views.index, name='index'),

    # /music/<album no(712)>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    # /music/<album_id>/favorite/>
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
