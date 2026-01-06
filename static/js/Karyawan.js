// static/js/karyawan.js

$(document).ready(function(){
    
    console.log('Karyawan module loaded');
    
    // ==========================================
    // Handle Form Submit dengan AJAX
    // ==========================================
    $('#formKaryawan').on('submit', function(e){
        e.preventDefault(); // Prevent default form submission
        
        // Ambil data dari form
        const formData = new FormData(this);
        
        // Get button
        const $btnSimpan = $('#btnSimpan');
        const originalText = $btnSimpan.html();
        
        // Disable button dan tampilkan loading
        $btnSimpan.prop('disabled', true)
                  .html('<i class="fas fa-spinner fa-spin me-2"></i>Menyimpan...');
        
        // Hide previous alert
        $('#alertMessage').addClass('d-none');
        
        // Kirim AJAX request ke Django
        $.ajax({
            url: '/input_karyawan/',  // URL endpoint Django
            type: 'POST',
            data: formData,
            processData: false,  // Jangan proses data
            contentType: false,  // Jangan set content type (biar auto)
            success: function(response){
                console.log('Response:', response);
                
                if(response.success){
                    // Tampilkan alert success
                    showAlert('success', response.message);
                    
                    // Reset form
                    $('#formKaryawan')[0].reset();
                    
                    // // Tutup modal setelah 1.5 detik dan reload
                    // setTimeout(function(){
                    //     $('#exampleModal').modal('hide');
                        
                    //     // Reload halaman untuk update tabel
                    //     location.reload();
                    // }, 1500);
                    
                } else {
                    // Tampilkan error dari server
                    showAlert('danger', response.message);
                }
            },
            error: function(xhr, status, error){
                console.error('Error:', error);
                console.error('Status:', xhr.status);
                console.error('Response:', xhr.responseText);
                
                // Ambil pesan error dari response
                let message = 'Terjadi kesalahan saat menyimpan data!';
                
                if(xhr.responseJSON && xhr.responseJSON.message){
                    message = xhr.responseJSON.message;
                } else if(xhr.status === 0){
                    message = 'Tidak dapat terhubung ke server!';
                } else if(xhr.status === 404){
                    message = 'URL endpoint tidak ditemukan!';
                } else if(xhr.status === 500){
                    message = 'Terjadi kesalahan pada server!';
                }
                
                showAlert('danger', message);
            },
            complete: function(){
                // Enable button kembali
                $btnSimpan.prop('disabled', false)
                          .html(originalText);
            }
        });
    });
    
    // ==========================================
    // Function: Show Alert
    // ==========================================
    function showAlert(type, message){
        const $alert = $('#alertMessage');
        
        $alert.removeClass('d-none alert-success alert-danger alert-warning alert-info')
              .addClass(`alert alert-${type}`)
              .html(`<i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'} me-2"></i>${message}`)
              .fadeIn();
        
        // Auto hide setelah 5 detik (kecuali success, karena akan reload)
        // if(type !== 'success'){
        //     setTimeout(function(){
        //         $alert.fadeOut(function(){
        //             $(this).addClass('d-none');
        //         });
        //     }, 5000);
        // }
    }
    
    // ==========================================
    // Reset form dan alert saat modal ditutup
    // ==========================================
    $('#exampleModal').on('hidden.bs.modal', function(){
        $('#formKaryawan')[0].reset();
        $('#alertMessage').addClass('d-none');
    });
    
    // ==========================================
    // Auto focus saat modal dibuka
    // ==========================================
    $('#exampleModal').on('shown.bs.modal', function(){
        $('#nama').focus();
    });
    
});