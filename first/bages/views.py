from django.http import request
from django.shortcuts import render
from . models import User, Message, Write_msg

# Create your views here.

 


def user (request):
    return render(request,'bages/index1.html' , {'ppl' : User.objects.all() })

def message (request):
   return render (request , 'bages/index1.html' , {'msg' : Message.objects.all()})

def index(request):
    urname = request.POST.get('your Name')
    urmsg = request.POST.get('your msg')
    data = Write_msg( urname = urname , urmsg = urmsg)
    if request.method == 'POST':
       x = data.save()
       if x.is_valid():
           x.save

    return render(request,'bages/index.html' )
 

  
 
 

