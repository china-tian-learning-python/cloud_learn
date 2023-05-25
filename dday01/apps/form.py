import re

from django.forms import Form,ModelForm
from . import models
from django import forms

from .models import PrettyNum


class departform(ModelForm):
    class Meta:
        model=models.UserInfo
        fields="__all__"

    def clean_name(self):
        name=self.cleaned_data.get("name")
        if name !="zeng":
            return name
        else:
            raise forms.ValidationError("该用户错误")
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs={"class":"form-control","placeholder":field.label}
class formdepart(Form):
    # name=forms.CharField(max_length=12,error_messages={"max_length":"test这是测试error_messages"},widget=forms.TextInput)
    # pwd=forms.CharField(max_length=12,widget=forms.PasswordInput,)
    text_input = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '请输入','class':"helloword"}))
    number_input = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 0, 'max': 100}))
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
    checkbox = forms.BooleanField(widget=forms.CheckboxInput())
    select = forms.ChoiceField(choices=[('1', '选项1'), ('2', '选项2')], widget=forms.Select())
    radio_select = forms.ChoiceField(choices=[('1', '选项1'), ('2', '选项2')], widget=forms.RadioSelect())

    # def clean__text_input(self):
    #     text_input=self.cleaned_data.get()

class pretty(ModelForm):
    class Meta:
        model=PrettyNum
        fields="__all__"
        widgets={

        }
    def clean_mobile(self):
        mobile=self.cleaned_data.get('mobile')

        if len(mobile) != 11:
            raise forms.ValidationError("你输入的手机号应该11位的有效数值")

        ret=re.match(r"^1(3[0-9]|5[012356789]|7[1235678]|8[0-9])\d{8}$",mobile)
        if ret:
            return mobile
        else:
            raise forms.ValidationError("你输入的手机号无效")
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,field in self.fields.items():
            if name=="status":
                # field.widget=forms.Select(attrs={"class":"form-control","placeholder":field.label})
                # continue
                pass
            field.widget.attrs={"class":"form-control","placeholder":field.label}

class admin(ModelForm):
    # render_value=True,
    pwd=forms.CharField(label="确认密码",max_length=32,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"确认密码"}))
    class Meta:
        model=models.admins
        fields=['username','password','pwd']
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"用户名"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"密码"})
        }
    def clean_username(self):
        username=self.cleaned_data.get("username")
        sql=models.admins.objects.filter(username=username)
        # 可以制定唯一约束
        if sql:
            raise forms.ValidationError("该用户已存在")
        else:
            return username
    def clean_pwd(self):
        pwd=self.cleaned_data.get("pwd")
        password=self.cleaned_data.get("password")
        if pwd==password:
            return pwd
        else:
            raise forms.ValidationError("密码不一致")

class admins(ModelForm):
    # render_value=True,
    # pwd=forms.CharField(label="确认密码",max_length=32,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"确认密码"}))
    class Meta:
        model=models.admins
        fields=['username']
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"用户名"}),

        }
    def clean_username(self):
        username=self.cleaned_data.get("username")
        sql=models.admins.objects.filter(username=username)
        # 可以制定唯一约束
        if sql:
            raise forms.ValidationError("该用户已存在")
        else:
            return username

class admin_change_pwd(ModelForm):
    # render_value=True,
    pwd=forms.CharField(label="确认密码",max_length=32,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"确认密码"}))
    class Meta:
        model=models.admins
        fields=['password','pwd']
        widgets={

            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"密码"})
        }
    def clean_password(self):
        password = self.cleaned_data.get("password")
        test = models.admins.objects.filter(id=self.instance.pk, password=password).exists()
        if test:
            raise forms.ValidationError("密码不能跟旧密码一致")
        else:
            return password
    def clean_pwd(self):
        pwd=self.cleaned_data.get("pwd")
        password=self.cleaned_data.get("password")
        if pwd==password:
            return pwd
        else:
            raise forms.ValidationError("密码不一致")

class admins_login(forms.Form):
    username=forms.CharField(max_length=32,widget=forms.TextInput(attrs={"class":"input-item","placeholder":"username"}))
    password=forms.CharField(max_length=32,widget=forms.PasswordInput(attrs={"class":"input-item","placeholder":"password"}))

