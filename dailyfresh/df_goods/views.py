#coding:utf-8
from django.shortcuts import render,redirect
from df_user.user_decoratior import inner
from django.core.paginator import Paginator,Page
from df_goods.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    t1_click = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:4]
    t1_new = GoodsInfo.objects.filter(gtype_id=1).order_by('-id')[0:4]
    t3_click = GoodsInfo.objects.filter(gtype_id=3).order_by('-gclick')[0:4]
    t3_new = GoodsInfo.objects.filter(gtype_id=3).order_by('-id')[0:4]
    t4_click = GoodsInfo.objects.filter(gtype_id=4).order_by('-gclick')[0:4]
    t4_new = GoodsInfo.objects.filter(gtype_id=4).order_by('-id')[0:4]
    t5_click = GoodsInfo.objects.filter(gtype_id=5).order_by('-gclick')[0:4]
    t5_new = GoodsInfo.objects.filter(gtype_id=5).order_by('-id')[0:4]
    t6_click = GoodsInfo.objects.filter(gtype_id=6).order_by('-gclick')[0:4]
    t6_new = GoodsInfo.objects.filter(gtype_id=6).order_by('-id')[0:4]

    context={'title':'首页',
             't1_click':t1_click,'t1_new':t1_new,
             't3_click':t3_click,'t3_new':t3_new,
             't4_click':t4_click,'t4_new':t4_new,
             't5_click':t5_click,'t5_new':t5_new,
             't6_click':t6_click,'t6_new':t6_new,
             }
    return render(request,'df_goods/index.html',context)

#采用ajax的方式来提交数据
def index_ajax(request,nid):
    t1_click = GoodsInfo.objects.filter(gtype_id=nid).order_by('-gclick')[0:4]
    t1_new = GoodsInfo.objects.filter(gtype_id=nid).order_by('-id')[0:4]
    click_list=[]
    for cl in t1_click:
        click_list.append({'id':cl.id,'title':cl.gtitle})
    new_list=[]
    # 获取图片的路径需要  name  这点要注意
    for cl in t1_new:
        new_list.append({'id':cl.id,'title':cl.gtitle,'price':cl.gprice,'pic':cl.gpic.name})
    context = {'click_list': click_list, 'new_list': new_list}
    return JsonResponse(context)



def detail(request):
    return render(request,'df_goods/detail.html')
@inner
def list(request,nid,Ipage,sort):
    ty_info = TypeInfo.objects.get(pk=int(nid))
    news_list = GoodsInfo.objects.filter(gtype_id=int(nid)).order_by('-id')[0:2]
    if sort == '1':
        sf_list = GoodsInfo.objects.filter(gtype_id=int(nid)).order_by('-id')
    elif sort == '2':
        sf_list = GoodsInfo.objects.filter(gtype_id=int(nid)).order_by('-gprice')
    elif sort == '3':
        sf_list = GoodsInfo.objects.filter(gtype_id=int(nid)).order_by('-gclick')
    pageinator = Paginator(sf_list,10)
    page = pageinator.page(int(Ipage))

    content_list =[]
    for v in sf_list:
        content_list.append({'gtitle':v.gtitle,'pic':v.gpic.name,'price':v.gprice})
    # 最新的两个
    new_list = []
    for v in news_list:
        new_list.append({'gtitle':v.gtitle,'pic':v.gpic.name,'price':v.gprice,'gunit':v.gunit})
    # print content
    content={'title':'商品列表',
             'content':content_list,
             'pageinator':pageinator,
             'page':page,
             'new_list':new_list,
             'ty_info':ty_info,
             'sort':sort}
    return render(request,'df_goods/list.html',content)
