import unittest
import turtle  # if you actually need turtle

from file_pendukung import assetlab_T1_navigasirobot_wrapper
from file_pendukung.assetlab_T1_navigasirobot_wrapper import TITIK_B

from jawaban_akhir.jawabanmu_T1_navigasirobot import namarobotmu


class TestRobotMovement(unittest.TestCase):
    def test_robot_reaches_destination(self):
        # Memeriksa apakah koordinat akhir robot mendekati Titik B
        koordinat_akhir = namarobotmu.turtle.pos()
        jarak_ke_tujuan = ((koordinat_akhir[0] - TITIK_B[0])**2 + (koordinat_akhir[1] - TITIK_B[1])**2)**0.5
        
        self.assertLess(jarak_ke_tujuan, 10, "Robotmu tidak sampai ke area tujuan :c")
        
        print("Robot berhasil sampai di area tujuan :D ! 🎉")

if __name__ == '__main__':
    unittest.main()
    turtle.bye() 
    sys.exit()
