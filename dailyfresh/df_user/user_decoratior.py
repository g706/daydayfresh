#coding:utf-8
from django.shortcuts import render,redirect

# has_key 用来判断这个user_id存在不存在
# get_full_path  全路径

def inner(func):
    def ouder(request,*args,**kwargs):
        if request.session.has_key('user_id'):
            return func(request,*args,**kwargs)
        else:
            red = redirect('/user/login')
            red.set_cookie('url',request.get_full_path())
            return red
    return ouder