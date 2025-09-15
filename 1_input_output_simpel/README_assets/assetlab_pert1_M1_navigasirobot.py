import turtle
import math

# Titik Awal & Titik Akhir
TITIK_A = (0, 0)
TITIK_B = (200, 200)

# Rintangan yang harus dihindari robot
# Format: (x, y, radius_tabrakan)
LIST_RINTANGAN = [
    (100, 50, 10),
    (150, 150, 15)
]

class Robot:
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.gambar_rintangan()
        self.gambar_tujuan()
        self.turtle.speed(1)
        self.turtle.penup()
        self.turtle.goto(TITIK_A)
        self.turtle.pendown()
        self.koordinat_jejak = [TITIK_A]
        

    def maju(self, langkah):
        self.turtle.forward(langkah)
        self.koordinat_jejak.append(self.turtle.pos())
        self.cek_tabrakan()

    def mundur(self, langkah):
        self.turtle.backward(langkah)
        self.koordinat_jejak.append(self.turtle.pos())
        self.cek_tabrakan()

    def putar_kanan(self, derajat):
        self.turtle.right(derajat)

    def putar_kiri(self, derajat):
        self.turtle.left(derajat)
        
    def gambar_tujuan(self):
        # Gambar titik awal (Titik A)
        turtle.penup()
        turtle.goto(TITIK_A)
        turtle.dot(10, "green")
        
        # Gambar titik akhir (Titik B)
        turtle.penup()
        turtle.goto(TITIK_B)
        turtle.dot(20, "green")
        
        turtle.pencolor("black")
        self.turtle.penup()
        self.turtle.goto(TITIK_A)
        self.turtle.pendown()
        
    def restart(self):
        self.turtle.reset()  # Mereset turtle ke posisi dan kondisi default
        self.koordinat_jejak = [self.turtle.pos()]
        self.gambar_rintangan() # Gambar rintangan lagi setelah direset
        self.gambar_tujuan()   # Gambar tujuan lagi
        print("Robot sudah di-reset. Silakan berikan perintah baru.")

        
    def gambar_rintangan(self):
        turtle.speed(0)  # Mengatur kecepatan gambar menjadi yang tercepat
        turtle.hideturtle()
        turtle.pensize(2)
        turtle.pencolor("red")
        
        for rintangan in LIST_RINTANGAN:
            x, y, radius = rintangan
            turtle.penup()
            turtle.goto(x, y - radius)
            turtle.pendown()
            turtle.circle(radius)
            turtle.penup()
            
    def cek_tabrakan(self):
        for rintangan in LIST_RINTANGAN:
            for jejak in self.koordinat_jejak:
                jarak = math.sqrt((jejak[0] - rintangan[0])**2 + (jejak[1] - rintangan[1])**2)
                if jarak < rintangan[2]:
                    raise RuntimeError("AAAAA! Robotmu nabrak woy!")
    
    def tunggu(self):
        turtle.done()
