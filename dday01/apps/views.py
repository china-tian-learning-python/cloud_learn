from django.shortcuts import render,redirect,reverse,HttpResponse
# Create your views here.
from django.views.decorators import csrf
from django.http.response import JsonResponse
from django.views import View
from . import models
from .form import departform, formdepart, pretty, admin, admins, admin_change_pwd, admins_login
from django.utils.safestring import mark_safe
from .utils import pags
class home(View):
    def get(self,request):
        data_dict=models.Department.objects.all()
        return render(request,'base.html',{'data_dict':data_dict})

class departadd(View):
    def get(self,request):
        return render(request,'depart_add.html')
    def post(self,request):
        title=request.POST.get('title')
        models.Department.objects.create(title=title)
        return redirect(reverse('home'))
class departput(View):
    def get(self,request,pk):

        data=models.Department.objects.get(id=pk)
        return render(request,'depart_put.html',{"data":data})
    def post(self,request,pk):
        models.Department.objects.filter(pk=pk).update(title=request.POST.get('title'))
        return redirect(reverse('home'))
def funs(request):
    ids=request.GET.get("id")
    depart=models.Department.objects.get(id=ids)
    depart.delete()
    return redirect(reverse('home'))

class userlist(View):
    def get(self,request):
        user_list=models.UserInfo.objects.all()
        return render(request,'user_list.html',{"user_list":user_list})

class useradd(View):
    def get(self,request):

        count={
            "sixs":models.UserInfo.choicess,
            "depart":models.Department.objects.all()
        }
        return render(request,'user_add.html',count)
    def post(self,request):
        name=request.POST.get('name')
        password=request.POST.get('password')
        age=request.POST.get('age')
        account=request.POST.get('account')
        create_time=request.POST.get("create_time")
        depart=request.POST.get("depart")
        six=request.POST.get("six")
        models.UserInfo.objects.create(name=name,password=password,age=age,account=account,create_time=create_time,depart_id=depart,six=six)
        return redirect(reverse('user_list'))

class usermodelform(View):
    def get(self,request):
        form=departform()
        return render(request,'usermodelform.html',locals())

    def post(self,request):
        form=departform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_list'))
        else:
            return render(request,'usermodelform.html',locals())
class userform_put(View):
    def get(self,request,pk):
        datas=models.UserInfo.objects.filter(pk=pk).first()
        form=departform(instance=datas)
        return render(request,'user_put.html',locals())
    def post(self,request,pk):
        datas=models.UserInfo.objects.filter(pk=pk).first()
        form=departform(data=request.POST,instance=datas)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_list'))
        else:
            return render(request, 'user_put.html', locals())

def user_delete(request,pk):
    models.UserInfo.objects.filter(pk=pk).first().delete()
    return redirect(reverse('user_list'))

class prettyList(View):
    def get(self,request):
        dicts={}
        # li_list=[]
        # page=int(request.GET.get("page","1"))
        # start_number=10*(page-1)
        # end_number=10*(page)
        # counts=models.PrettyNum.objects.count()
        # sum_number,remainder=divmod(counts,10)
        # if remainder:
        #     sum_number+=1
        # page_number=5
        # #数据库较少，没有达到11页时
        # if sum_number<=2*page_number+1:
        #     #最小页数
        #     page_start=1
        #     #最大页数位数据库页数
        #     page_end=sum_number
        # else:
        #     #数据库超过11页时
        #     #判断当前页数是否小于5
        #     if page<=page_number:
        #         #如果小于5，则最小与最大固定在（1，11）之间
        #         page_start=1
        #         page_end=2*page_number+1
        #         print('hello world')
        #     elif page + page_number >= sum_number:
        #         page_start = sum_number - 2 * page_number
        #         page_end = sum_number
        #     else:
        #             page_start=page-page_number
        #             page_end=page+page_number
        #         #判断当前页数+5是否超过最大页数
        # # 首页
        # str = '<li><a href="?page={}">首页</a></li>'.format(1)
        # li_list.append(str)
        # #上一页
        # if page>1 :
        #     str='<li><a href="?page={}">上一页</a></li>'.format(page-1)
        # else:
        #     str = '<li><a href="?page={}">上一页</a></li>'.format(1)
        # li_list.append(str)
        #
        # print(page_start,page_end)
        # for li in range(page_start,page_end+1):
        #     #没有固定的10码数  需要判断是否超过页码数
        #         if li==page:
        #             str = '<li class="active" ><a href="?page={}">{}</a></li>'.format(li, li)
        #         else:
        #             str='<li><a href="?page={}">{}</a></li>'.format(li,li)
        #
        #         li_list.append(str)
        #
        #     #下一页
        # if page < sum_number:
        #     str = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
        # else:
        #     str = '<li><a href="?page={}">下一页</a></li>'.format(sum_number)
        # li_list.append(str)
        #
        # #尾页
        # str = '<li><a href="?page={}">尾页</a></li>'.format(sum_number)
        # li_list.append(str)
        # str_li_list=''.join(li_list)
        # str_li_list=mark_safe(str_li_list)
        search_data=request.GET.get("search","")
        if search_data:
            dicts["mobile__contains"]=search_data
        pretty_list=models.PrettyNum.objects.filter(**dicts)
        woos=pags(request,sqls=pretty_list)
        pretty_list=woos.queryset
        str_li_list=woos.html()
        return render(request,'pretty_list.html',locals())

class prettyAdd(View):
    def get(self,request):
        form=pretty()
        return render(request,'pretty_add.html',locals())
    def post(self,request):
        form=pretty(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pretty_list'))
        else:
            return render(request,'pretty_add.html',locals())
class prettyPut(View):
    def get(self,request,pk):
        datas=models.PrettyNum.objects.filter(pk=pk).first()
        form=pretty(instance=datas)
        return render(request,'pretty_put.html',locals())
    def post(self,request,pk):
        datas=models.PrettyNum.objects.filter(pk=pk).first()
        form=pretty(instance=datas,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pretty_list'))
        else:
            return render(request, 'pretty_put.html', locals())

def pretty_delete(request,pk):
    models.PrettyNum.objects.filter(pk=pk).first().delete()
    return redirect(reverse('pretty_list'))
class tests(View):

    def get(self,request):
        form=formdepart()
        return render(request,'test.html',locals())

class admin_list(View):

    def get(self,request):
        dicts = {}
        username = request.GET.get("search", "")
        if username:
            dicts['username__contains'] = username
        woo = models.admins.objects.filter(**dicts)
        pages = pags(request, sqls=woo)
        str_li_list = pages.html()
        admin_list = pages.queryset
        return render(request,'admin_list.html',locals())

class admin_add(View):
    def get(self,request):
        form=admin()
        return render(request,'admin_add.html',locals())

    def post(self,request):
        form=admin(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_list'))
        else:
            return render(request, 'admin_add.html', locals())
class admin_put(View):
    def get(self,request,pk):
        form=admins(instance=models.admins.objects.filter(pk=pk).first())
        return render(request,'admin_put.html',locals())
    def post(self,request,pk):
        form=admins(data=request.POST,instance=models.admins.objects.filter(pk=pk).first())
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_list'))
        else:
            return render(request,'admin_put.html',locals())
def admin_delete(request,pk):
    models.admins.objects.filter(pk=pk).first().delete()
    return redirect(reverse('admin_list'))

class admin_change(View):
    def get(self, request, pk):
        form = admin_change_pwd()
        return render(request, 'admin_change.html', locals())

    def post(self, request, pk):
        form = admin_change_pwd(instance=models.admins.objects.filter(pk=pk).first(),data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('admin_list'))
        else:
            return render(request, 'admin_change.html', locals())

class login(View):
    def get(self,request):
        form=admins_login()
        print(form)
        print('hello world')
        return render(request,'login.html',locals())
    def post(self,request):
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        form=admins_login(request.POST)
        if form.is_valid():
            test=models.admins.objects.filter(**form.cleaned_data).first()
            if test:
                request.session['info']={"id":test.id,"username":test.username}
                return redirect(reverse('home'))
            else:
                print(form.cleaned_data)
                form.add_error(field='password',error="账号或密码错误")
                return render( request,'login.html',locals())

def logout(request):
    request.session.clear()
    return redirect(reverse('admin_list'))


def admin_test(request):
    return render(request,'test.html')

def admin_ajax(request):
    print("hello world")
    return JsonResponse({"message":"ok"})