from django.shortcuts import render
from .models import RapArt
from django.db.models import Q


def start(request):
    return render(request, 'main/start.html')


def list_rap(request):
    search_r = request.GET.get('search', '')
    if search_r:
        rap = RapArt.objects.filter(Q(name__icontains=search_r) | Q(description__icontains=search_r))
    else:
        rap = RapArt.objects.all()
    return render(request, 'main/listrap.html', {'rap': rap})


def raper(request, id_r):
    one = RapArt.objects.get(id=id_r)
    return render(request, 'main/raper.html', {'one': one})


def search_r(request, id_r):
    one = RapArt.objects.get(id=id_r)
    return render(request, 'main/raper.html', {'one': one})
