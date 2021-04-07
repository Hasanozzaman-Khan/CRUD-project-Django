from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import studentRegistration
from enroll.models import User

# Create your views here.

# This function will add new record and show all record
def add_show(request):
    if request.method == 'POST':
        fm = studentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = studentRegistration()
    else:
        fm = studentRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})


# Update function
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = studentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = studentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form':fm})


# Delete function
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
