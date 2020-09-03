from django.urls import path,include
from . import views


urlpatterns = [

    path('/', views.Quiz),
    path('quiz/', include('Quiz.urls'))
]