from django.shortcuts import render
from TODOApp.api.serializers import TODOSerializer
from TODOApp.models import TODO
from rest_framework.generics import ListAPIView, CreateAPIView,UpdateAPIView,DestroyAPIView

class TODOList(ListAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class TODOCreate(CreateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class TODOUpdate(UpdateAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

class TODODestroy(DestroyAPIView):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
