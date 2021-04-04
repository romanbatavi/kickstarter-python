######################################################
# Nama file: datastatis.py
######################################################

class Kotak(object):

   ObjectCounter = 0

   def __init__(self, p, l, t):
      self.panjang = p
      self.lebar = l
      self.tinggi = t
      # setiap objek dibuat, ObjectCounter
      # dinaikkan satu
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

def main():
   # membuat objek pertama
   kotak1 = Kotak(6, 5, 4)
   # menggunakan objek pertama
   print("Objek pertama")
   kotak1.cetakData()
   kotak1.cetakVolume()
   print("ObjectCounter = ", kotak1.ObjectCounter)

   # membuat objek kedua
   kotak2 = Kotak(10, 8, 6)
   # menggunakan objek kedua
   print("\nObjek kedua")
   kotak2.cetakData()
   kotak2.cetakVolume()
   print("ObjectCounter = ", kotak2.ObjectCounter)

   # membuat objek ketiga
   kotak3 = Kotak(4, 3, 2)
   # menggunakan objek ketiga
   print("\nObjek ketiga")
   kotak3.cetakData()
   kotak3.cetakVolume()
   print("ObjectCounter = ", kotak3.ObjectCounter)

   # memanggil kembali nilai ObjectCounter
   print("\nObjectCounter pada objek pertama = ", 
          kotak1.ObjectCounter)
   print("ObjectCounter pada objek kedua = ", 
          kotak2.ObjectCounter)
   print("ObjectCounter pada objek ketiga = ", 
          kotak3.ObjectCounter)

if __name__ == "__main__":
   main()
