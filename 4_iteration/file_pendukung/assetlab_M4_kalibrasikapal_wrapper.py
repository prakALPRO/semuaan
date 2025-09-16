"""
file class untuk soal M4 me-rekalibrasi kapal yang ada di tempat antah berantah sehingga bisa pulang.

16 Sept 2025

jojo. with help from Google's Gemini :>
"""


import turtle
import math
import random


# Rintangan yang bisa dimunculkan
# Format: (x, y, radius_tabrakan)
LIST_RINTANGAN = [
    (100, 50, 10),
    (150, 150, 15),
    (-100, -150, 20),
    (50, -100, 12)
]

class Kapal:
    """
    A class to manage a ship and lighthouse simulation.
    It spawns both at random positions.
    """
    def __init__(self, bounds=400):
       
        self.screen = turtle.Screen()
        self.screen.title("Ship to Lighthouse")
        self.screen.bgcolor("skyblue")
        
        self.bounds = bounds
        
        self.kapal = turtle.Turtle()
        self.kapal.shape("turtle")
        self.kapal.color("darkgreen")
        self.kapal.speed(0)
        self.kapal.penup()
        
        # Create the lighthouse turtle
        self.mercusuar = turtle.Turtle()
        self.mercusuar.shape("circle")
        self.mercusuar.color("red")
        self.mercusuar.penup()
        

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
        

    def spawn_ship_randomly(self, bounds=200):
        """Spawns the ship at a random location."""
        x = random.randint(-bounds, bounds)
        y = random.randint(-bounds, bounds)
        self.turtle.goto(x, y)
        self.turtle.setheading(random.randint(0, 360))
        self.turtle.pendown()
        
    def spawn_lighthouse_randomly(self, bounds=200):
        """Spawns the ship at a random location."""
        lighthouse_x = random.randint(-self.bounds, self.bounds)
        lighthouse_y = random.randint(-self.bounds, self.bounds)
        self.mercusuar.goto(lighthouse_x, lighthouse_y)
        self.mercusuar.dot(20, "green")
        
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
                    raise RuntimeError("AAAAA! kapalmu nabrak karang woy!")

    def cek_sampai_lighthouse(self):
        
    
    def tunggu(self):
        turtle.done()
