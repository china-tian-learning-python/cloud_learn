from django.db import models

# Create your models here.

class Department(models.Model):
    title=models.CharField("标题",max_length=32)
    class Meta:
        db_table='department'
        verbose_name="部门表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
class UserInfo(models.Model):
    choicess=(
        (1,'男'),
        (2,'女')
    )
    name=models.CharField("姓名",max_length=16)
    password=models.CharField("密码",max_length=64)
    age=models.IntegerField("年龄")
    account=models.DecimalField("账号余额",max_digits=10,decimal_places=2)
    create_time=models.DateField("入职时间")
    depart=models.ForeignKey(to="Department",on_delete=models.CASCADE)
    six=models.SmallIntegerField("性别",choices=choicess)
    class Meta:
        db_table='userinfo'
        verbose_name="员工表"
        verbose_name_plural=verbose_name


class PrettyNum(models.Model):
    level_choices=(
        ("1", "1级"),("2", "2级"),("3", "3级"),("4", "4级")
    )

    mobile=models.CharField('手机号',max_length=11)
    price=models.FloatField('价格',null=True,blank=True)
    level=models.CharField('靓号等级',choices=level_choices,max_length=12)
    status=models.BooleanField("是否使用",default=True)

    class Meta:
        db_table='pretty'


class admins(models.Model):

    username=models.CharField("用户名",max_length=32)
    password=models.CharField("密码",max_length=32)

    class Meta:
        db_table='admins'
        verbose_name="管理员"
        verbose_name_plural=verbose_name
