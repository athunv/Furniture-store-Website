from django.urls import path
from account import views
from .views import lgout


urlpatterns = [
    
    path("login",views.LoginView.as_view(),name="login"),
    path("register",views.RegView.as_view(), name='register'),
    path('logout',lgout,name='logout')
]