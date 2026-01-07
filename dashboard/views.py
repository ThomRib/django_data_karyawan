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
	
	return render(request, 'dashboard/data_karyawan.html')

# tambah data
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
		
# tampilkan data
def get_karyawan(request):
    try:
        hasil = koneksi.cursor_fetch_result(
            "SELECT nama, email, posisi, departemen FROM karyawan"
        )

        print("=== DEBUG HASIL ===")
        print(type(hasil))
        print(hasil)
        print("==================")

        # hasil adalah LIST of DICT
        if not hasil:
            return JsonResponse({
                'success': True,
                'data': [],
                'message': 'Belum ada data karyawan'
            })

        data_json = []
        for idx, row in enumerate(hasil, start=1):
            data_json.append({
                'no': idx,
                'nama': row['nama'].strip(),
                'email': row['email'].strip(),
                'posisi': row['posisi'].strip(),
                'departemen': row['departemen'].strip(),
            })

        return JsonResponse({
            'success': True,
            'data': data_json
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({
            'success': False,
            'data': [],
            'message': str(e)
        }, status=500)

# delete data
def delete_karyawan(request):
    if request.method != 'POST':
        return JsonResponse({'success': False}, status=405)

    email = request.POST.get('email')

    if not email:
        return JsonResponse({
            'success': False,
            'message': 'Email tidak ditemukan'
        }, status=400)

    koneksi.cursor_execute_commit(
        "DELETE FROM karyawan WHERE email=%s",
        [email]
    )

    return JsonResponse({
        'success': True,
        'message': 'Data berhasil dihapus'
    })

# update data
def update_karyawan(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        nama = request.POST.get('nama')
        posisi = request.POST.get('posisi')
        departemen = request.POST.get('departemen')

        koneksi.cursor_execute_commit(
            """
            UPDATE karyawan
            SET nama=%s, posisi=%s, departemen=%s
            WHERE email=%s
            """,
            [nama, posisi, departemen, email]
        )

        return JsonResponse({
            'success': True,
            'message': 'Data berhasil diperbarui'
        })

    return JsonResponse({'success': False}, status=400)
		
def logout_view(request):
	"""Logout user"""
	# TODO: Implement logout logic
	return render(request, 'dashboard/index.html')