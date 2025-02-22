from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


# Create your views here.


# home page
def home(request):
    return render(request, "webapp/index.html")


# register
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # once registered redirect to login page
            return redirect("my_login")
    return render(request, "webapp/register.html", context={"form": form})


# user login
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # return redirect('')
    return render(request, "webapp/my-login.html", context={"form": form})
