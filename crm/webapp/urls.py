from django.urls import path
from . import views


urlpatterns = [
    # render home view
    path("", views.home, name=""),
    path("register/", views.register, name="register"),
    path("my-login/", views.my_login, name="my_login"),
]
