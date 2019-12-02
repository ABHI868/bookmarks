from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html' ,{'section':'dashboard'} )



def user_login(request):
    if request.method =='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            user=authenticate(username = cd['username'] , password = cd['password'])
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Logged In Successfully !')
                else:
                    return HttpResponse('Account has been disabled ')
            else:
                return HttpResponse('User does not Exist')
    else:
        form=LoginForm()
        return render(request , 'account/login.html',{'form' :form}) 



def register(request):
  
    if request.method=='POST':
        userform= UserRegistrationForm(request.POST)
        if userform.is_valid():
            new_user=userform.is_save(commit=False)
            new_user.set_password(userform.cleaned_data['password'])
            new_user.save()
            return render(request,'registration/registration_done.html',{'new_user':new_user})
    else: 
            
        print('register getting called')

        userform=UserRegistrationForm()
        print('hi')
        return render(request, 'registration/register.html',{'user_form':userform})