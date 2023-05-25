from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from . import models
from . import tests
from django.views import View
from django.http import HttpResponse,JsonResponse
from django.db.models import Avg, Count
from django.core.serializers import serialize

# items={'title': 'SolidWorks2020中文版机械设计从入门到精通', 'text': '《SOLIDWORKS □0□0中文版机械设计从入门到精通》详细介绍了SOLIDWORKS □0□0在机械设计中的应用方法和技巧。全书共17章，主要包括SOLIDWORKS □0□0概述、草图绘制、3D草图和3D曲线、参考几何', 'name': 'CAD，CAM，CAE技术联盟', 'press_name': '清华大学出版社', 'date': '2020-10-1', 'price': '74.80'}
from . import models


class test(View):
    def get(self,request):


        book=list(models.Books.objects.values('press__id').annotate(prices=Avg('price')).values('press__press_name','prices'))
        # 统计每位作者书籍数量
        boos=list(models.Author.objects.annotate(number=Count('author__title')).values('name','number').order_by('-number'))
        wood=models.Books.objects.filter(date__month='3').all()
        cc=list(models.Books.objects.values("date__month").annotate(number=Count('title')).values('date__month',"number"))
        # print(boos)
        # to=models.Books.objects.all()
        # print(to)
        # boos=serialize('json',cc)
        return JsonResponse(cc,safe=False)
        # data_list=tests.funs()
        # for items in data_list:
        #     sta = models.Author.objects.filter(name__contains=items["name"]).exists()
        #     if sta:
        #         authors = models.Author.objects.filter(name__contains=items["name"]).first()
        #         sta2 =models.Press.objects.filter(press_name=items['press_name']).exists()
        #         if sta2:
        #             presss = models.Press.objects.filter(press_name=items["press_name"]).first()
        #             presss.author.add(authors.id)
        #             models.Books.objects.create(title=items['title'],text=items['text'],price=float(items['price']),date=items['date'],author_id=authors.id,press=presss)
        #             # return HttpResponse("已存在2")
        #         presss = models.Press.objects.create(press_name=items["press_name"])
        #         presss.author.add(authors.id)
        #         models.Books.objects.create(title=items['title'],
        #                                     text=items['text'],
        #                                     price=float(items['price']),
        #                                     date=items['date'],
        #                                     author_id=authors.id,
        #                                     press=presss
        #                                     )
        #         # return HttpResponse("已存在")
        #     else:
        #         models.Author.objects.create(name=items["name"])
        #         authors = models.Author.objects.filter(name=items["name"]).first()
        #
        #         sta2 = models.Press.objects.filter(press_name=items['press_name']).exists()
        #         if sta2:
        #             presss = models.Press.objects.filter(press_name=items["press_name"]).first()
        #             presss.author.add(authors.id)
        #             models.Books.objects.create(title=items['title'],
        #                                         text=items['text'],
        #                                         price=float(items['price']),
        #                                         date=items['date'],
        #                                         author_id=authors.id,
        #                                         press=presss
        #                                         )
        #             # return HttpResponse("已存在3")
        #         else:
        #             presss = models.Press.objects.create(press_name=items["press_name"])
        #             presss.author.add(authors.id)
        #             models.Books.objects.create(title=items['title'],
        #                                         text=items['text'],
        #                                         price=float(items['price']),
        #                                         date=items['date'],
        #                                         author_id=authors.id,
        #                                         press=presss
        #                                         )
        # return HttpResponse("ok")


class tests(View):
    def get(self,request):
        return render(request,'test.html',locals())
    def post(self,request):
        # wo=open('wa.txt','wb')
        # data=request.FILES.get("text")
        # wa=models.Files(name="zeng",wen=data)
        # wa.save()
        # for li in data.chunks():
        #     wo.write(li)
        # wo.close()
        wo_path=FileSystemStorage().save(request.FILES.get('text').name,request.FILES.get('text'))
        models.Files.objects.create(name="tian",wen=wo_path)
        return HttpResponse('ok')