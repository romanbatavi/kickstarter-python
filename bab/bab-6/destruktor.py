######################################################
# Nama file: destruktor.py
######################################################

# mendefinisikan kelas
class Kotak(object):
   def __init__(self, p, l, t):
      print("Konstruktor Kotak dipanggil")
      self.panjang = p
      self.lebar = l
      self.tinggi = t
   def __del__(self):
      print("Destruktor Kotak dipanggil")      
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
   # membuat objek
   kotak = Kotak(6, 5, 4)

   # menggunakan objek
   kotak.cetakData()
   kotak.cetakVolume()

   # menghapus objek secara manual
   del kotak

if __name__ == "__main__":
   main()
