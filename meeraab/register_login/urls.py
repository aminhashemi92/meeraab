from django.urls import path
from .views import *


app_name = "register_login"
urlpatterns = [
    path('', register_login, name="register_login"),
    path('logout/',logoutUser,name="logout"),
    # path('changeprofile',changeprofile,name="changeprofile"),
    # path('changepassword',changepassword,name="changepassword"),

]
