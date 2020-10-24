"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from Quiz import views
from Search import views as search_views
from Vaccine import views as vaccine_views


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.password, name = 'Login'),
    path('home', views.home, name = 'Home'),
    path('about', views.about, name = 'About'),
    path('readmore',views.readMore, name = 'Read More'),
    path('quizlist/quizstart',views.evaluation, name = 'Evaluation'),
    path('quizlist/getuserchoice', views.getUserChoice, name = 'Review1'),
    path('quizlist/quizintro', views.quizIntro, name='Quiz Intro'),
    path('quizlist/quizcategory', views.quizCategory, name='Quiz List'),
    path('search', search_views.searchClinic, name='Search'),
    path('search/searchresult', search_views.searchResult, name='Search Result'),
    path('vaccine', vaccine_views.vaccine, name='Vaccine'),
    path('prevention', vaccine_views.prevention, name = 'Prevention'),
    path('prevention/airquality', vaccine_views.airquality, name = 'Air Quality'),
    path('prevention/healthhabit', vaccine_views.health_habit, name = 'Health Habit'),
    path('test',search_views.test,name='Test')

]
urlpatterns += staticfiles_urlpatterns()