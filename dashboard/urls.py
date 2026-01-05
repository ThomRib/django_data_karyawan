from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data_karyawan/', views.data_karyawan, name='data_karyawan'),
    path('input_karyawan/', views.input_karyawan, name='input_karyawan'),
    path('logout/', views.logout_view, name='logout'),
]