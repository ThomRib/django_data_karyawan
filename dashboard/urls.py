from django.urls import path
from . import views

urlpatterns = [
    
    # Authentication URLs
    # path('login/', views.indexlogin, name='login'),
    # path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('', views.index, name='index'),
    path('data_karyawan/', views.data_karyawan, name='data_karyawan'),

    # Ajax
    path('get_karyawan/', views.get_karyawan, name='get_karyawan'),
    path('delete_karyawan/', views.delete_karyawan, name='delete_karyawan'),
    path('input_karyawan/', views.input_karyawan, name='input_karyawan'),
    path('update_karyawan/', views.update_karyawan, name='update_karyawan'),

]