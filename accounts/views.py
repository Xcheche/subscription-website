from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "accounts/index.html")

def login_view(request):
    pass

def logout_view(request):
    pass

def register_view(request):
    pass
