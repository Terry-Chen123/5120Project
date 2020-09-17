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


from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'Home'),
    path('about/', views.about, name = 'About'),
    path('service/',views.service, name = 'Service'),
    path('readmore/',views.readMore, name = 'Read More'),
    path('service/quizlist/quizstart',views.evaluation, name = 'Evaluation'),
    path('service/quizlist/getuserchoice', views.getUserChoice, name = 'Review1'),
    path('service/quizlist/quizintro', views.quizIntro, name='Quiz Intro'),
    path('service/quizlist/quizcategory', views.quizCategory, name='Quiz List'),
    path('service/search', views.searchClinic, name='Search'),
    path('service/search/searchresult', views.searchResult, name='Search Result'),
    path('test',views.test,name='Test')

]
urlpatterns += staticfiles_urlpatterns()