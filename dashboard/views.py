from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    """Dashboard utama"""
    context = {
        # Data untuk dashboard
    }
    return render(request, 'dashboard/index.html', context)

def data_karyawan(request):
    """Halaman daftar karyawan"""
    # TODO: Ambil data dari database
    karyawan_list = []
    
    context = {
        'karyawan_list': karyawan_list
    }
    return render(request, 'dashboard/data_karyawan.html', context)

def input_karyawan(request):
    """Halaman input karyawan baru"""
    if request.method == 'POST':
        # TODO: Simpan data ke database
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        posisi = request.POST.get('posisi')
        departemen = request.POST.get('departemen')
        gaji = request.POST.get('gaji')
        
        # Simpan ke database
        messages.success(request, 'Data karyawan berhasil disimpan!')
        return redirect('dashboard:data_karyawan')
    
    return render(request, 'dashboard/input_karyawan.html')

def logout_view(request):
    """Logout user"""
    # TODO: Implement logout logic
    return redirect('dashboard:index')