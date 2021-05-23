from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, UserComments, BdayComment
import sys
import django


def index(request):
    '''
    for i in UserComments.objects.all():
        i.delete()
    '''
    pics = Image.objects.all()
    pics = list(pics)
    img_clr = ['b017e7f', 'bc11a2b', 'b68ff00',
               'b052939', 'bFFBF00', 'bff005c']
    length = len(pics)
    a = []
    while len(a) < length:
        a += img_clr
    a = a[:length]
    ziplist = zip(pics, a)
    return render(request, 'index.html', {'ziplist': ziplist})


def puzzle(request):
    bcomments = BdayComment.objects.all()
    img_clr = ['red', 'orange', 'violet', 'purple', '#006FFF',
               '#13f4ef', '#68ff00', '#faff00', '#FFBF00', '#ff005c']
    length = len(bcomments)
    a = []
    while len(a) < length:
        a += img_clr
    a = a[:length]
    ziplist = zip(bcomments, a)
    return render(request, 'puzzle.html', {'bcomments': bcomments, 'ziplist': ziplist})


def comment(request):
    if request.method == 'POST':
        username = request.POST['username']
        comment = request.POST['comment']
        ins = UserComments(username=username, comment=comment)
        ins.save()
        print(username, comment)
        usercomments = UserComments.objects.all()
        img_clr = ['red', 'orange', 'violet', 'purple', '#006FFF',
                   '#13f4ef', '#68ff00', '#faff00', '#FFBF00', '#ff005c']
        length = len(usercomments)
        a = []
        while len(a) < length:
            a += img_clr
        a = a[:length]
        ziplist = zip(usercomments, a)
        return render(request, 'comment.html', {'ziplist': ziplist})
    usercomments = UserComments.objects.all()
    img_clr = ['red', 'orange', 'violet', 'purple', '#006FFF',
               '#13f4ef', '#68ff00', '#faff00', '#FFBF00', '#ff005c']
    length = len(usercomments)
    a = []
    while len(a) < length:
        a += img_clr
    a = a[:length]
    ziplist = zip(usercomments, a)
    return render(request, 'comment.html', {'ziplist': ziplist})
