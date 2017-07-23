#coding=utf-8
from django.shortcuts import render,redirect,HttpResponse
from hashlib import sha1
from django.http import JsonResponse
from models import *
from df_user.user_decoratior import  inner
# Create your views here.

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登陆','error_name':0,'error_pwd':0,'uname':uname }
    return render(request,'df_user/login.html',context)

def login_hander(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu')
    user = UserInfo.objects.filter(uname=uname)
    print user,uname
    if len(user)==1:
        s1 = sha1()
        s1.update(upwd)
        pwd = s1.hexdigest()
        # 此出说明密码是一样的
        if pwd == user[0].upwd:
            url = request.COOKIES.get('url','/')
            red = redirect(url)
            # 登陆成功删除原来cookie失效时间
            red.set_cookie('url','',max_age=0)
            if jizhu !=0:
                red.set_cookie('uanem',uname)
            else:
                red.set_cookie('url', '', max_age=0)
            request.session['user_id']=user[0].id
            request.session['user_name']= uname
            return red
        else:
            context = {'title':'用户登陆','error_name': 0,'error_pwd': 1,'uname':uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        context = {'title': '用户登陆', 'error_name': 1, 'error_pwd': 0, 'uname': uname, 'upwd': upwd}
        return render(request, 'df_user/login.html', context)



def register(request):
    context = {'title':'用户注册'}
    return render(request,'df_user/register.html',context)
#处理用户注册
def register_hanld(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    if upwd != upwd2:
        return redirect('/user/register')
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()
    print upwd3,uname
    # 存到数据库中
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    return redirect('/user/login')
# ajax校验存在的用户名
def register_exist(requset):
    uname = requset.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def logout(request):
    request.session.flush()
    return redirect('/')
@inner
def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).uemail
    return render(request,'df_user/user_center_info.html')

@inner
def order(request):
    return render(request,'df_user/user_center_order.html')

@inner
def site(request):
    return render(request,'df_user/user_center_site.html')









