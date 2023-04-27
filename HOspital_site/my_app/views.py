from django.shortcuts import render, HttpResponseRedirect
from .form import myform, loginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

UserModel = get_user_model()
# Create your views here.


def Ragisterform(request):
    if request.method == "POST":
        fm = myform(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Ragistration Successfully !!!')
            fm = myform()
    else:
        fm = myform()
    return render(request, 'SignUp.html', {'form':fm})

def LoginForm(request):
        if request.method == 'POST':
            lg = loginForm(request=request, data=request.POST)
            if lg.is_valid():
                nm = lg.cleaned_data['username']
                pw = lg.cleaned_data['password']
                user = authenticate(username=nm, password=pw)
                if user is not None:
                    login(request, user)
                    
                    return HttpResponseRedirect('/profile/')
        else:
            lg = loginForm()
        return render(request, 'login.html', {'form':lg})

@login_required
def profile(request):
    if request.user.catagory == 'Patient':
        user = UserModel.objects.filter(email=request.user.email)
        print(user)
        return render(request, 'patient.html', {'user': user})
    user = UserModel.objects.filter(email=request.user.email)
    print(user)
    return render(request, 'doctor.html', {'user': user})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')
