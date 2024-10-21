from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Board


# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


 # Make sure Board is imported correctly


def boards_topics(request, board_id):
    # try:
    #     board = Board.objects.get(pk=board_id)
    # except Board.DoesNotExist:
    #     raise Http404  # This will return a 404 page if the board doesn't exist
    board=get_object_or_404(Board,pk=board_id)
    return render(request, 'topics.html', {'board': board})
def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'new_topic.html', {'board': board})