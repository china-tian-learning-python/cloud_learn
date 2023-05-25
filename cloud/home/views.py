from django.shortcuts import render
from django.views import View
# Create your views here.
from . import models


class CloudView(View):
    def get(self,request):
        one = models.One.objects.all().values()
        print(one)
        return render(request,"test.html")

class OneView(View):
    def get(self,request):
        search =request.GET.get("search","")
        if search:
            one_data=models.One.objects.filter(title__icontains=search).all()
            return render(request,'one.html',locals())
        else:
            one_data = models.One.objects.all()
            return render(request,'one.html',locals())

class TwoView(View):
    def get(self,request):
        search = request.GET.get("search", "")
        if search:
            two_data = models.Two.objects.filter(title__icontains=search).all()
            return render(request, 'two.html', locals())
        else:
            two_data = models.Two.objects.all()
            return render(request, 'two.html', locals())

class ThreeView(View):
    def get(self,request):
        search = request.GET.get("search", "")
        if search:
            three_data = models.Three.objects.filter(title__icontains=search).all()
            return render(request, 'three.html', locals())
        else:
            three_data = models.Three.objects.all()
            return render(request, 'three.html', locals())

class FourView(View):
    def get(self,request):
        search = request.GET.get("search", "")
        if search:
            four_data = models.Four.objects.filter(title__icontains=search).all()
            return render(request, 'four.html', locals())
        else:
            four_data = models.Four.objects.all()
            return render(request, 'four.html', locals())
