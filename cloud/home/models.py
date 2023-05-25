from django.db import models


# Create your models here.

# 单选题
class One(models.Model):
    title = models.CharField("题目", max_length=500)
    A = models.CharField("选项A", max_length=256)
    B = models.CharField("选项B", max_length=256)
    C = models.CharField("选项C", max_length=256)
    D = models.CharField("选项D", max_length=256)
    an = models.CharField("答案", max_length=500)

    class Meta:
        db_table = "one"


# 多选题
class Two(models.Model):
    title = models.CharField("题目", max_length=500)
    A = models.CharField("选项A", max_length=256)
    B = models.CharField("选项B", max_length=256)
    C = models.CharField("选项C", max_length=256)
    D = models.CharField("选项D", max_length=256)
    an = models.CharField("答案", max_length=600)

    class Meta:
        db_table = "two"


# 填空题
class Three(models.Model):
    title = models.CharField("题目", max_length=600)
    an = models.CharField("答案", max_length=600)

    class Meta:
        db_table = "three"


# 简答题
class Four(models.Model):
    title = models.CharField("题目", max_length=600)
    an = models.TextField("答案")

    class Meta:
        db_table = "four"
