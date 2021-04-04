######################################################
# Nama file: metode.py
######################################################

# mendefinisikan kelas
class Kotak(object):
   def __init__(self, p, l, t):
      self.panjang = p
      self.lebar = l
      self.tinggi = t
   def hitungVolume(self):
      return self.panjang * self.lebar * \
             self.tinggi
   def cetakData(self):
      print("panjang\t: ", self.panjang)
      print("lebar\t: ", self.lebar)
      print("tinggi\t: ", self.tinggi)
   def cetakVolume(self):
      print("Volume\t= ", self.hitungVolume())

def main():
   # membuat objek pertama
   kotak1 = Kotak(6, 4, 3)

   # menggunakan objek pertama
   print("Objek kotak1")
   kotak1.cetakData()
   kotak1.cetakVolume()

   # membuat objek kedua
   kotak2 = Kotak(5, 3, 2)

   # menggunakan objek kedua
   print("\nObjek kotak2")
   kotak2.cetakData()
   kotak2.cetakVolume()

if __name__ == "__main__":
   main()
