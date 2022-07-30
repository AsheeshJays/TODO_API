from django.shortcuts import redirect, render,HttpResponseRedirect
from .models import TODO
from .forms import TODOFORM

def IndexPage(request):
    item = TODO.objects.all()
    if request.method == 'POST':
        to = TODO()
        to.item = request.POST.get('item')
        to.save()
    return render(request, 'index.html',{'item':item})


def DeleteItem(request, id):
    item = TODO.objects.get(pk=id)
    item.delete()
    return HttpResponseRedirect('/')

def EditItem(request, id):
    i = TODO.objects.get(pk=id)
    if request.method == 'POST':
        i.item = request.POST.get('item')
        i.save()
        return redirect('/')
    return render(request, 'update.html',{'item':i})