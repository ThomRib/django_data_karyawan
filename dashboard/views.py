from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from . import koneksi

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
		try:
			# TODO: Simpan data ke database
			nama = request.POST.get('nama')
			email = request.POST.get('email')
			posisi = request.POST.get('posisi')
			departemen = request.POST.get('departemen')
			
				
			# Validasi data
			if not all([nama, email, posisi, departemen]):
				return JsonResponse({
					'success': False,
					'message': 'Semua field harus diisi!'
				}, status=400)
			
			# Debug print
			print(f"Nama: {nama}")
			print(f"Email: {email}")
			print(f"Posisi: {posisi}")
			print(f"Departemen: {departemen}")
			
			hasil = koneksi.cursor_execute_commit("INSERT INTO karyawan (nama, email, posisi, departemen) VALUES ( %s, %s, %s, %s )",[nama,email,posisi,departemen])
			print(hasil)
			
			# tes koneksi
			# koneksi.cek_db_default()
			
			# print('Data karyawan berhasil disimpan!')
			
			# Return JSON response untuk AJAX
			return JsonResponse({
				'success': hasil['status'],
				'message': hasil['message']
			})
			
		except Exception as e:
			print(f"Error: {str(e)}")
			return JsonResponse({
				'success': False,
				'message': f'Terjadi kesalahan: {str(e)}'
			}, status=500)

	

def logout_view(request):
	"""Logout user"""
	# TODO: Implement logout logic
	return redirect('dashboard:index')