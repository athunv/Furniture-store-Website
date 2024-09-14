from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView,CreateView
from .forms import LoginForm,RegForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout


class IndexView(TemplateView):

    template_name = 'index.html'


class LoginView(FormView):

    template_name = "login.html"
    form_class = LoginForm


    def post(self,request,*args,**kw):

        form_data = LoginForm(data=request.POST)
        if form_data.is_valid():
            user = form_data.cleaned_data.get('username')
            pswd = form_data.cleaned_data.get('password')
            user_obj=authenticate(request,username=user,password=pswd)
            if user_obj:
                login(request,user_obj)
                messages.success(request,"Login Success!!")
                return redirect('userhome')
            else:
                messages.error(request,"Login Faild!!")
                return redirect('login')
        messages.info(request,"Invalid username or password !!")
        return render(request,'login.html',{"form":form_data})
        

class RegView(CreateView):
    
    template_name = "register.html"
    form_class = RegForm
    success_url = reverse_lazy('login')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request,"Registration Successfully!!")
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        messages.error(self.request,"Registration Faild!!")
        return super().form_invalid(form)
    
def lgout(request):
    logout(request)
    messages.success(request,'Loged out successfully')
    return redirect('login')