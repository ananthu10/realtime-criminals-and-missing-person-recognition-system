from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
   username = forms.CharField(widget=TextInput(attrs={'class': 'user-box', 'placeholder': 'Email'}))
   password = forms.CharField(widget=PasswordInput(attrs={'class':'user-box'}))



def logout_view(request):
   logout(request)
   return redirect('login')

def login_view(request):
   error_message=None
   form=AuthenticationForm()
   if request.method=='POST':
      form=AuthenticationForm(data=request.POST)
      if form.is_valid():
         username=form.cleaned_data.get('username')
         password=form.cleaned_data.get('password')
         user=authenticate(username=username,password=password)
         if user is not None:
            login(request,user)
            if request.GET.get('next'):
               return redirect(request.GET.get('next'))
            else:
               return redirect('faceuploader:index')
         else:
            error_message='Ups ... somthing went wrong'
   context={
         'form':form,
         'error_message':error_message
      }
   return render(request,'auth/login.html',context)