from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField("作者", max_length=320,)

    class Meta:
        db_table = 'author'


class Books(models.Model):
    title = models.CharField("书名", max_length=320)
    text = models.TextField("简介")
    price = models.FloatField("价格")
    date = models.DateField("时间")
    author = models.ForeignKey(to='Author', verbose_name='作者', on_delete=models.CASCADE, related_name='author')
    press = models.ForeignKey(to='Press', verbose_name="出版社", on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'
'''
  authors=models.Author.objects.create(name=items["name"])
  authors=models.Author.objects.create(name=items["name"])
  presss=models.Press.objects.create(press_name=items["press_name"])
  presss.author.add()
'''

# 出版社
class Press(models.Model):
    press_name = models.CharField('出版社名称', max_length=320)
    author = models.ManyToManyField(to='Author', verbose_name="作者id")

    class Meta:
        db_table = 'press'

class Files(models.Model):
    name=models.CharField("文件名称",max_length=32)
    wen=models.FileField("文件路径",upload_to="wood/%Y%m%d")
    class Meta:
        db_table='files'