from django.shortcuts import render, redirect

from accounts.forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    return render(request, "accounts/index.html")

def login_view(request):
    pass

def logout_view(request):
    pass

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CreateUserForm()

    return render(request, "accounts/register.html", {"form": form})



#login authenticate with AuthenticationForm

def login(request):

    form = AuthenticationForm()

    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username') # Username / Email
            password = request.POST.get('password')

            # Username / Email

            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_writer==True:

                login(request, user)

                return redirect('writer-dashboard')


            if user is not None and user.is_writer==False:

                login(request, user)

                return redirect('client-dashboard')


    context = {'LoginForm': form}

    return render(request, 'account/login.html', context)


def user_logout(request):

    logout(request)

    return redirect("login")
