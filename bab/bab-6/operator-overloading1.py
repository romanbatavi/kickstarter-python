######################################################
# Nama file: operator-overloading1.py
######################################################

# mendefinisikan kelas BilanganBulat
class BilanganBulat(object):
   def __init__(self, nilai):
      if not isinstance(nilai, int):
         raise TypeError("Nilai harus bertipe bilangan bulat")
      self.nilai = nilai

   # overload terhadap operator +
   def __add__(self, objek):
      if isinstance(objek, int):
         return self.nilai + objek
      elif isinstance(objek, float):
         return float(self.nilai + objek)
      elif isinstance(objek, BilanganBulat):
         return self.nilai + objek.nilai
      else:
         raise TypeError("Objek harus bertipe numerik")

def main():
   # objek dari kelas BilanganBulat
   a = BilanganBulat(10)
   b = BilanganBulat(20)

   # objek bertipe int
   c = 30

   # objek bertipe float
   d = 40.75

   # menggunakan operator +
   print(a + b)
   print(a + c)
   print(a + d)

if __name__ == "__main__":
   main()
