from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages


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
            # show message
            messages.success(request, "Account Created Successfully!")
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
                # show message
                messages.success(request, "Logged In!")
                return redirect("dashboard")
    return render(request, "webapp/my-login.html", context={"form": form})


# dashboard
@login_required(login_url="my_login")
def dashboard(request):
    my_records = Record.objects.all()
    context = {"records": my_records}
    return render(request, "webapp/dashboard.html", context=context)


# add a record
@login_required(login_url="my_login")
def create_record(request):
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            # show message
            messages.success(request, "Record Created!")
            return redirect("dashboard")
    return render(request, "webapp/create-record.html", context={"form": form})


# update a record
@login_required(login_url="my_login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated!")
            return redirect("dashboard")

    return render(request, "webapp/update-record.html", context={"form": form})


# read or view a singular record
@login_required(login_url="my_login")
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)
    return render(request, "webapp/view-record.html", {"record": all_records})


# user logout
def user_logout(request):
    auth.logout(request)
    # show message
    messages.success(request, "Logged Out!")
    return redirect("my_login")


# delete a record
@login_required(login_url="my_login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    # show message
    messages.success(request, "Record Deleted!")
    return redirect("dashboard")
