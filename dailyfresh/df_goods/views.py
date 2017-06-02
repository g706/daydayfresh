#coding:utf-8
from django.shortcuts import render,redirect

# Create your views here.
def index(request):

    return render(request,'df_goods/index.html')