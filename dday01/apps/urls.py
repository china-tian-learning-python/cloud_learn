from django.urls import path
from . import views
urlpatterns=[
path('',views.home.as_view(),name='home'),
path('add',views.departadd.as_view(),name="adds"),
path('delete',views.funs,name='delete'),
path('put/<int:pk>',views.departput.as_view(),name='put'),

path('user/list',views.userlist.as_view(),name='user_list'),
path('user/add',views.useradd.as_view(),name='user_add'),
path('user/add2',views.usermodelform.as_view(),name='user_add2'),
path('user/add3',views.tests.as_view(),name='test'),
path('user/put/<int:pk>',views.userform_put.as_view(),name='user_put'),
path('user/delete/<int:pk>',views.user_delete,name='user_delete'),

path('pretty/list',views.prettyList.as_view(),name='pretty_list'),
path('pretty/add',views.prettyAdd.as_view(),name='pretty_add'),
path('pretty/put/<int:pk>',views.prettyPut.as_view(),name='pretty_put'),
path('pretty/delete/<int:pk>',views.pretty_delete,name='pretty_delete'),

    path('admin/list',views.admin_list.as_view(),name='admin_list'),
    path('admin/add',views.admin_add.as_view(),name='admin_add'),
    path('admin/put/<int:pk>',views.admin_put.as_view(),name='admin_put'),
    path('admin/delete/<int:pk>',views.admin_delete,name="admin_delete"),
    path('admin/change/<int:pk>',views.admin_change.as_view(),name="admin_change"),
    path('admin/login',views.login.as_view(),name='admin_login'),
    path('admin/logout',views.logout,name='admin_logout'),
    path('admin/test',views.admin_test,name='admin_test'),
    path('admin/ajax',views.admin_ajax,name='admin_ajax')
]