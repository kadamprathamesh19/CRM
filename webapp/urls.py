
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home, name=""),

    path('register',views.register, name="register"),

    path('my-login',views.my_login, name="my-login"),

    path('user_logout',views.user_logout, name="user_logout"),


    # -- CRUD Operations

    path('dashboard',views.dashboard, name="dashboard"),

    path('create-record',views.create_record, name="create-record"),

    path('update-record/<int:pk>',views.update_record, name="update-record"),
    
    path('singular-record/<int:pk>',views.singular_record, name="singular-record"),

    path('delete-record/<int:pk>',views.delete_record, name="delete-record"),

    


]


# password:
# admin = raj/123456789
# user = man1/p123456789
