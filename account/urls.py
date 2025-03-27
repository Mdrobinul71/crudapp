from django.urls import path
from account.views import register,user_login,user_logout


urlpatterns=[
    path('register/',register,name='sign_up'),
    path('login/',user_login,name="user_login"),
    path('logout/',user_logout,name="user_logout"),

]