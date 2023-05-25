from django.urls import path
from . import views
urlpatterns=[
    path('',views.tests.as_view(),name="test"),

]
