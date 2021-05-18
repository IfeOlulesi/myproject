from django.shortcuts import render, get_object_or_404

from .models import Board


def home(request):
    boards = Board.objects.all()

    return render(request, 'home.html', {'boards': boards})

def board_topics(request, id):
    board = get_object_or_404(Board, pk=id)
    return render(request, 'topics.html', {'board': board})