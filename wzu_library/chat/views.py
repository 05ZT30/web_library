from django.shortcuts import render, redirect
import uuid
from .models import Message
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    uid4 = uuid.uuid4().hex
    return render(request, 'chat/index.html', {'uid4': uid4})


def room(request, room_name):
    chat_messages = Message.objects.filter(group_name=room_name).order_by("created")[:100]
    return render(request, 'chat/room.html', {
        'chat_messages': chat_messages,
        'room_name': room_name
    })

def chat(request):
    if not request.session.get('is_login', None):
        return login_required(TemplateView.as_view(template_name='base.html'))
    else:
       return redirect('/index/')