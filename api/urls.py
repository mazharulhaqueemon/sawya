from django.urls import path
from api import views
urlpatterns=[
    path('',views.index),
    path('api/',views.funcbaseapiview,name='function base for get request'),# views.funcion name for functiuon base api
    path('api/<int:pk>',views.funcbaseapiview,name ='function base api for delete ,update and put'),
    path('apiclass/',views.classBaseApiView.as_view(),name='class base for get request'),# views.callassbaseapi.as_view() for class base api view
    path('apiclass/<int:pk>',views.classBaseApiView.as_view(),name ='class base api for delete ,update and put'),


]