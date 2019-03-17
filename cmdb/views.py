from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from cmdb import models
import json
import os
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from decimal import Decimal
from django.http import HttpResponse


def login(request):
    if request.method == 'POST':
        ret = {'code': 1000, 'msg': '成功登陆'}
        try:
            datalist = request.body.decode('utf-8')
            data = json.loads(datalist)
            username = data['username']
            password = data['password']
            # user = request.POST.get('username')
            # pwd = request.POST.get('password')
            # a1=json({"username":user,"password":pwd})
            obj = models.UserInfo.objects.filter(username=username, password=password)
            if obj:
                for a in obj:
                    ret['role'] = a.role
            else:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
        return JsonResponse(ret)


def register(request):
    if request.method == 'POST':
        msg = {"message": "注册完毕"}
        datalist1 = request.body.decode('utf-8')
        data = json.loads(datalist1)
        user = data['username']
        password = data['password']
        tel = data['tel']
        role = data['role']
        models.UserInfo.objects.create(username=user, password=password, tel=tel, role=role)
        return JsonResponse(msg)


def MySQL(request):
    if request.method == "POST":
        msg = {"number": 10}
        myFile = request.FILES['file']  # 直接根据file取出来angular中返回到后端的值
        if not myFile:
            msg["number"] = 20
            return JsonResponse(msg)
        destination = open(os.path.join("C://Users/xiaoygao/PycharmProjects/untitled1", myFile.name), 'wb+')
        for chunk in myFile.chunks():  # 分块使用二进制的方式写入文件
            destination.write(chunk)
        destination.close()
        with open(myFile.name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                models.Show.objects.create(name=row[0], shopname=row[1], price=row[2], pinglun=row[3])
            msg["number"] = 30
            return JsonResponse(msg)
        msg["number"] = 40
        return JsonResponse(msg)


def search(request):
    test = {"accept": 250}
    if request.method == "POST":
        datalist = request.body.decode('utf-8')
        data = json.loads(datalist)
        # if data["input"]=="gaoxiaoyu":
        #     test['accept']=100
        #     return JsonResponse(test)
        # return JsonResponse(test)
        res = data['input']
        blogs = models.Show.objects.filter(name__contains=res)
        # res1 = []
        # for a in blogs:
        # print(a.name)
        # 预留一列记录查询次数
        # # obj = models.Show.objects.get(name=res)
        #     hit = obj.hit
        #     hit += 1
        #     models.Show.objects.filter(name=res).update(hit=hit)
        if blogs:
            res1 = []
            for a in blogs:
                # res1.append(a.name)
                # res2.append(a.shopname)
                res1.append({
                    'name': a.name,
                    'shopname': a.shopname,
                    'price': a.price,
                    'pinglun': a.pinglun
                })
            # json.loads(res1)
            # name_json={}
            # name_json=dict(zip(res1,res2))
            return JsonResponse(res1, safe=False)
            # 必须要加这个safe 要不他认为你这个json不安全
            ###############################################
        # res1={}
        # for a in blogs:
        #     res1['name']=a.name
        #     res1['shopname']=a.shopname
        #     res1['price']=a.price
        #     res1['pinglun']=a.pinglun
        # print(res1)
        # return JsonResponse(res1)
        ##############################################
        # res2.append(res1)
        # return HttpResponse(json.dumps(res1),content_type="application/json")
        # if blogs:
        #     obj = models.Show.objects.get(name=res)
        #     hit = obj.hit
        #     hit += 1
        #     models.Show.objects.filter(name=res).update(hit=hit)
        #     return JsonResponse(test)


def searchtrue(request):
    if request.method == 'POST':
        datalist = request.body.decode('utf-8')
        data = json.loads(datalist)
        res = data['searchthing']
        # print(type(res[0]))
        res2 = res[0].strip()
        print(res2)
        blogs = models.Show.objects.filter(name=res2)
        # error={'code':100}
        print(blogs)
        if blogs:
            obj = models.Show.objects.get(name=res2)
            hit = obj.hit
            hit += 1
            models.Show.objects.filter(name=res2).update(hit=hit)
        res1 = {}
        for a in blogs:
            res1['name'] = a.name
            res1['shopname'] = a.shopname
            res1['price'] = a.price
            res1['pinglun'] = a.pinglun
        print(res1)
        return JsonResponse(res1)
        # return JsonResponse(error)


def Hcharts(request):
    if request.method == 'GET':
        name_list = []
        hit_list = []
        for a in models.Show.objects.order_by('-hit')[:5]:
            name_list.append(a.name)
            hit_list.append(a.hit)
        name_json = {}
        name_json = dict(zip(name_list, hit_list))
        # data=list(zip(name_list,hit_list))
        return JsonResponse(name_json)


def Hcharts1(request):
    if request.method == 'GET':
        name_list = []
        price_list = []
        for a in models.Show.objects.order_by('-hit')[:5]:
            name_list.append(a.name)
            price_list.append(a.price)
        name_json = {}
        name_json = dict(zip(name_list, price_list))
        # data=list(zip(name_list,hit_list))
        return JsonResponse(name_json)


def Hcharts2(request):
    if request.method == 'GET':
        name_list = []
        pinglun_list = []
        for a in models.Show.objects.order_by('-hit')[:5]:
            name_list.append(a.name)
            pinglun_list.append(a.pinglun)
        name_json = {}
        name_json = dict(zip(name_list, pinglun_list))
        # data=list(zip(name_list,hit_list))
        return JsonResponse(name_json)
