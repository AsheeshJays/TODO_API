from django.urls import path
from TODOApp.api import views

urlpatterns = [
    path('todoList/',views.TODOList.as_view(),name='todolist'),
    path('todoCreate/',views.TODOCreate.as_view(),name='todocreate'),
    path('todoUpdate/<int:pk>/',views.TODOUpdate.as_view(),name='todoupdate'),
    path('todoDestroy/<int:pk>/',views.TODODestroy.as_view(),name='tododestroy'),
]
