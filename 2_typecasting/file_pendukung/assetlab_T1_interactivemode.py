from assetlab_T1_navigasirobot_wrapper import Robot

robot = Robot()

heading_keren = """
  _____    _   _    ____      _      ____            _    
 |_ " _|U |"|u| |U /"___|uU  /"\  u / __"| u        /"|   
   | |   \| |\| |\| |  _ / \/ _ \/ <\___ \/       u | |u  
  /| |\   | |_| | | |_| |  / ___ \  u___) |        \| |/  
 u |_|U  <<\___/   \____| /_/   \_\ |____/>>        |_|   
 _// \\_(__) )(    _)(|_   \\    >>  )(  (__)     _//<,-, 
(__) (__)   (__)  (__)__) (__)  (__)(__)         (__)(_/                                            

  versi interaktif untuk debugging.
  kontrol robotnya dengan sequence gerakan supaya dia bisa berhenti di posisi target
  
   Robot siap! 
  
  KETIK PERINTAH DI TERMINAL INI UNTUK MENGONTROL ROBOTNYA! :D


Untuk perintah yang menggunakan (x), ganti x dengan angka yang diinginkan (misalnya, maju(50)). Angka ini menentukan seberapa jauh atau seberapa besar sudut putar robot.

maju(x)         : Untuk bergerak maju sejauh x pixel
mundur(x)       : Untuk bergerak mundur sejauh x pixel
putar_kanan(x)  : Untuk berputar ke kanan sebesar x derajat
putar_kiri(x)   : Untuk berputar ke kiri sebesar x derajat

restart         : Mengulang program dan mereset penghitung perintah.
q               : Menghentikan program dan keluar.
  
============================================================                                                                         
"""

print(heading_keren)

perintah_ke = 1 # Inisialisasi penghitung perintah
while True:
    perintah = input(f"\nPerintah {perintah_ke}: ")

    # Perintah Q untuk keluar
    if perintah.lower() == 'q':
        print("Robot dimatikan.")
        time.sleep(1) # Beri waktu untuk melihat pesan
        turtle.bye()
        break
    
    # Perintah RESTART untuk mengulang
    elif perintah.lower() == 'restart':
        perintah_ke = 0
        print("Sistem di-restart.")
        robot.restart()
    
    # Menangani perintah robot dan kesalahan
    try:
        # Menjalankan perintah (misalnya maju(50))
        eval(f"robot.{perintah}")
        
        # Cek tabrakan setelah perintah berhasil
        robot.cek_tabrakan()
        
        # Tambah penghitung jika semuanya berhasil
        perintah_ke += 1
        
    except RuntimeError as e:
        # Menangani kesalahan tabrakan secara spesifik
        print(f"Error: {e} 💥")
        
        print("Sistem di-restart.")
        robot.restart()
        
        perintah_ke = 1

    except Exception as e:
        # Menangani semua kesalahan lainnya (seperti perintah tidak valid)
        print(f"Error: Perintah tidak valid. {e}")

