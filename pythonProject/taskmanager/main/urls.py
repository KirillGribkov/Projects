#from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'main'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('main.urls'))
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),

]
