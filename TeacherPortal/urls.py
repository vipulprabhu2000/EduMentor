from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user,name='login_user'),
    path('HomePage/',views.Home,name='Home'),
    path('logout/',views.logout_user,name='logout_user'),
    path('Add/',views.Add_Student,name='Add_Student'),
    path('Delete_Student/<str:name>/<str:subject>/<str:marks>/',views.Delete_Student,name='Delete_Student'),
]
