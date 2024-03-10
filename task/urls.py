from django.contrib import admin
from django.urls import path,include
from .views import registration, login
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.mainpage,name='mainpage.html'),
    path('registration.html', views.registration, name='registration.html'),
    path('login.html', views.login, name='login.html'),
    path('dash.html',views.dash,name='dash.html'),
    path('forgot.html',views.forgot,name='forgot.html'),
    path('addtask.html',views.addtask,name='addtask.html'),
    path('viewtask.html',views.viewtask,name='viewtask.html'),
    path('calendar.html',views.calendar,name='calendar.html'),
]
