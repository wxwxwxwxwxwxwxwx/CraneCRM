from django.shortcuts import render
from . models import Articles
from django.http import HttpResponseRedirect, HttpResponse
from docxtpl import DocxTemplate
import io
from io import BytesIO
from django.http import FileResponse
from docxtpl import DocxTemplate


def index(request):
   return render(request, 'main/index.html')


def articles(request):
   Articles = Articles.objects.all()
   return render(request, 'main/Articles.html', context={'Articles': Articles})   

   

  


 
