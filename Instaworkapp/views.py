from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Adddata
from Instaworkapp.forms import AddForm


# Create your views here.


def listview(request):
    total_list_count = Adddata.objects.all().count()
    total_list = Adddata.objects.all()
    return render(request, 'Instaworkapp/listdetail.html',
                  {'total_list_count': total_list_count, 'total_list': total_list})
    # return HttpResponse("Hello,World. You're at the polls index.")


def addview(request):
    addform = AddForm()
    if request.method == 'POST':
        # print(request.POST)
        addform = AddForm(request.POST)
        if addform.is_valid():
            addform.save()
            print("success")
            return redirect('Instaworkapp:listview')
    return render(request, 'Instaworkapp/addmembers.html', {'addform': addform})

def editview(request, id):
    data = Adddata.objects.get(id=id)
    editform = AddForm(instance=data)

    if request.method == 'POST':
        editform = AddForm(request.POST, instance=data)
        if editform.is_valid():
            editform.save()
            return redirect('Instaworkapp:listview')
        else:
            print(editform.errors.as_data())
            # raise forms.ValidationError(editform.errors)

    return render(request, 'Instaworkapp/editmembers.html', {'editform': editform, 'data': data, 'error': editform.errors.as_data()})

def deleteview(request, id):
    data= Adddata.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('Instaworkapp:listview')
    return render(request, 'Instaworkapp/deletemember.html', {'data': data})
