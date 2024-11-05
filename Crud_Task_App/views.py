from django.shortcuts import render, redirect, get_object_or_404

from Crud_Task_App.forms import Add_study_forms
from Crud_Task_App.models import AddStudy


# Create your views here.

def test2(request):
    return render(request,'Test.html')

def MainPageView(request):
    return render(request,'Mainpage.html')


def addStudy(request):
    form = Add_study_forms()
    if request.method=='POST':
        data = Add_study_forms(request.POST)
        if data.is_valid():
            data.save()
        return redirect('read')
    return render(request,'AddStudy.html',{'form':form})


def read(request):
    data = AddStudy.objects.all()
    return render(request,'Mainpage.html',{'read':data})


def update(request,id):
    data1 = AddStudy.objects.get(id=id)
    form1 = Add_study_forms(instance = data1)
    if request.method == 'POST':
        form1 = Add_study_forms(request.POST,instance=data1)
        if form1.is_valid():
            form1.save()
        return redirect('read')
    return render(request,'Update.html',{'variable':form1})


def delete(request,id):
    remove = AddStudy.objects.get(id=id)
    remove.delete()
    return redirect('read')

# def detailedView(request,id):
#     data = AddStudy.objects.get(id=id)
#     return render(request,'DetailedView.html',{'form':data})
def detailedView(request, id):
    data = get_object_or_404(AddStudy, id=id)
    return render(request, 'DetailedView.html', {'data': data})