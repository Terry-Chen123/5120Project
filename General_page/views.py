from django.shortcuts import render

# Create your views here.
def password(request):
    return render(request, "../templates/password.html")

def home(request):
    return render(request, "../templates/index.html")

def about(request):
    return render(request, "../templates/about.html")

