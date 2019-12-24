from django.shortcuts import render, redirect
from mess.models import Message
from .forms import MessageForm

def index(request):
    data = Message.objects.all()
    userform = MessageForm(request.POST)
    if userform.is_valid():
        userform.save()
        return redirect('index')

    return render(request, 'mess/index.html', {'data': data, 'form': userform})

