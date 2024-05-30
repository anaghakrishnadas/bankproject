from django.urls import path

from . import views
app_name='bank'
urlpatterns = [

    path('', views.home,name='home'),
    path('branch/<str:district>/', views.branch, name='branch'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('new/', views.NewPage, name='new'),
    path('form/', views.FormPage, name='form'),
    path('about/', views.about, name='about'),
    
]
