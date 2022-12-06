from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('watchlater', views.watchlater, name='watchlater'),
    path('history', views.history, name='history'),
    path('c/<str:channel>', views.channel, name='channel'),
    path('upload', views.upload, name='upload'),
    path('search', views.search, name='search'),
    path('album/', views.albums, name='albums'),
    path('album/<int:id>', views.albumpost, name='albumpost'),
    path('genre_list', views.genre_list, name='genre_list'),
    path('tags/<str:tags_name>', views.tags, name='tags'),
]
