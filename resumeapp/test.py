from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.urls import resolve
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import *
from django.db.models import Count,Sum

class demo(View):
    def get(self, request, *args, **kwargs):
        return render(request, "showtemplates.html",{'demo':request})

class demo_submit(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("Successfully Inserted!")