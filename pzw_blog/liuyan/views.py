from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from liuyan.models import Message
from liuyan.forms import MessageForm
import datetime

# Create your views here.

def index(request):
    messages = Message.objects.all()
    if request.method == 'GET':
        return render(request, 'liuyan/index.html', {'messages':messages})


def create(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            new_message = message_form.save(commit=False)
            new_message.publish = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            new_message.user = request.user
            new_message.save()
        return redirect('liuyan:index')
    else:
        return render(request,'liuyan/create.html',{'user':user})