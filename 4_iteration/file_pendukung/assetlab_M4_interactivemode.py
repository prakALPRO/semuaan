from assetlab_M1_navigasirobot_wrapper import Robot

robot = Robot()
print("Robot siap! Gunakan perintah 'maju(x)', 'mundur(x)', 'putar_kanan(x)', 'putar_kiri(x)'.")
print("Ketik 'q' dan enter untuk mengakhiri.")

perintah_ke = 1 # Inisialisasi penghitung perintah

while True:
    perintah = input(f"Perintah {perintah_ke}: ")
    if perintah.lower() == 'keluar':
        print("Robot dimatikan.")
        turtle.bye()
        break
    
    try:
        eval(f"robot.{perintah}")
        perintah_ke += 1 # Tambah penghitung hanya jika perintah berhasil
    except Exception as e:
        print(f"Error: Perintah tidak valid. {e}")

