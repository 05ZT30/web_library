from django.shortcuts import render,redirect
from .models import News
from .models import roll
from django.http import  HttpResponse

# Create your views here.
def index(request):
     new_list=News.objects.all()
     rollpic=roll.objects.all()

     context={
          'res':new_list.order_by('-time')[:5],
          'pic':rollpic.order_by('-add_date')[:5],
     }
     return render(request, 'index.html', context=context)

def detail(request,num):
     detail=News.objects.get(id=num)
     context={
          'detail':detail
     }
     return render(request,'news.html',context)