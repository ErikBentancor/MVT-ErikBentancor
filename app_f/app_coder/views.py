import http
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime, timedelta
from app_coder import models 
from django.shortcuts import render
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

def db(request):
    
    documentoDeTexto = f"--->Curso: "
    
    return render(request, 'appcoder/db.html')

def probar_template(request):
  
    fam= models.Familiar.objects.all()

    return render(request, 'appcoder/probar_template.html', {'li': fam})
