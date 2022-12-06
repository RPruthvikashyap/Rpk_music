from django.shortcuts import render
from musicbeats.models import Song

def index(request):
    return render(request, 'index.htm')
    return render(request, 'index.htm', {'song': Song})
from django.shortcuts import render
from django.db.models import Case, When
from django.contrib.auth.models import User
from musicbeats.models import Song
from musicbeats.models import Watchlater
from musicbeats.models import Album



def index(request):
    song = Song.objects.all()[0:4]
    album = Album.objects.all()[0:4]

    if request.user.is_authenticated:
        wl = Watchlater.objects.filter(user=request.user)
        ids = []
        for i in wl:
            ids.append(i.video_id)
        
        preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
        watch = Song.objects.filter(song_id__in=ids).order_by(preserved) 
        watch = reversed(watch)
    
    else:
        watch = Song.objects.all()[0:4]

    return render(request, 'index.htm', {'song': song, 'watch': watch, 'album':album})
