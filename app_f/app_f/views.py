import http
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime, timedelta
from app_coder import models 
from django.shortcuts import render

def db(request):
    pass

def probar_template(request):
  
    fam= models.Familiar.objects.all()

    return render(request, 'plantilla.html', {'li': fam})

  #  return HttpResponse(texto_html)
#def db_handle(request):
  #      user_list_obj = models.Demo.objects.all()
   #     return render(request, 't1.html', {'li': user_list_obj})
