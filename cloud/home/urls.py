from django.urls import path
from . import views
urlpatterns = [
    path('',views.CloudView.as_view(),name="home"),
    path('one',views.OneView.as_view(),name='one'),
    path("two",views.TwoView.as_view(),name='two'),
    path("three",views.ThreeView.as_view(),name='three'),
    path("four",views.FourView.as_view(),name='four')
]