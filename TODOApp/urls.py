from django.urls import path
from TODOApp import views

urlpatterns = [
    path('',views.IndexPage,name="Index"),
    path('delete/<int:id>/',views.DeleteItem,name='delete'),
    path('edit/<int:id>/',views.EditItem,name='edit')
]
