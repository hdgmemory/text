from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import T_ser
from datetime import datetime
# Create your views here.
def register (request):
    return render(request,'login.html')
def rg (request):
    return render(request,'home.html')
def route(re):
    return render(re,'route.html')
def faq(request):
    return render(request,'FAQ.html')
def add(rq):
    return render(rq,'teacher/add.html')
def tijiao(request):
    # 取表单数据
    title = request.POST['title']
    autor = request.POST['autor']
    #插入数据
    result =T_ser.objects.create(name=title,age=autor)
    # result.save()
    if result:
        return HttpResponseRedirect('teacher/xianshi')
    else:
        return HttpResponse('插入失败')

def xianshi(request):
    #查数据
    # list = T_ser.objects.all()
    list = T_ser.objects.order_by('name')
    return  render(request,'teacher/xianshi.html',{"ls":list})
def xq(rq,pk):
    atc = T_ser.objects.get(id=pk)
    return render(rq,'teacher/xq.html',{"at":atc})
def sc(rq,pk):
    ss = T_ser.objects.get(pk=pk)
    a = ss.delete()
    if a:
        return HttpResponse("删除成功")
    else:
        return HttpResponse("删除失败")