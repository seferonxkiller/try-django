from django.urls import path
from .views import *

app_name = 'article'
urlpatterns = [
    path('',index, name="list"),
    path('article/detail/<slug:slug>/',detail,name="detail"),
    path('article/create/',create,name="create"),
    path('article/edit/<slug:slug>/',edit,name="edit"),
    path('article/delete/<slug:slug>/',delete,name="delete")

]