######################################################
# Nama file: metodestatis.py
######################################################

class Kotak(object):
   # kelas variabel (data statis)
   ObjectCounter = 0

   def __init__(self, p, l, t):
      self.panjang = p
      self.lebar = l
      self.tinggi = t
      Kotak.ObjectCounter += 1

   def hitungVolume(self):
      return self.panjang * self.lebar * \
             self.tinggi

   def cetakData(self):
      print("panjang\t: ", self.panjang)
      print("lebar\t: ", self.lebar)
      print("tinggi\t: ", self.tinggi)

   def cetakVolume(self):
      print("Volume\t= ", self.hitungVolume())

   @staticmethod
   def cetakJudul():
      if Kotak.ObjectCounter > 1:
         print()  # baris baru
      print("KOTAK KE-", Kotak.ObjectCounter)

def main():
   k1 = Kotak(6, 5, 4)
   Kotak.cetakJudul()  # memanggil metode statis
   k1.cetakData()
   k1.cetakVolume()

   k2 = Kotak(5, 3, 2)
   Kotak.cetakJudul()  # memanggil metode statis
   k2.cetakData()
   k2.cetakVolume()

   k3 = Kotak(8, 6, 3)
   Kotak.cetakJudul()  # memanggil metode statis
   k3.cetakData()
   k3.cetakVolume()

if __name__ == "__main__":
   main()
