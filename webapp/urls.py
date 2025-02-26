from django.urls import path
from . import views


urlpatterns = [
    # render home view
    path("", views.home, name=""),
    path("register/", views.register, name="register"),  # register page
    path("my-login/", views.my_login, name="my_login"),  # login page
    path("user-logout/", views.user_logout, name="user_logout"),  # dashboard page
    # CRUD
    path("dashboard/", views.dashboard, name="dashboard"),  # dashboard page
    path("create-record/", views.create_record, name="create_record"),  # create record
    path("update-record/<int:pk>/", views.update_record, name="update_record"),
    path("record/<int:pk>/", views.singular_record, name="record"),
    path("delete-record/<int:pk>/", views.delete_record, name="delete_record"),
]
