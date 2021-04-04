######################################################
# Nama file: array1.py
######################################################

import sys

class Array(object):
   def __init__(self, arr=[]):
      self.data = arr
   
   def salin(self):
      temp = Array(self.data)
      return temp
   
   def tambah(self, nilai):
      if len(self.data) > 0:
         if type(self.data[0]) == type(nilai):
            self.data.append(nilai)
         else:
            print("Nilai yang ditambahkan harus sejenis")
            sys.exit(1)
   
   def ubah(self, indeks, nilai):
      self.data[indeks] = nilai
   
   def hapus(self, nilai):
      self.data.remove(nilai)
   
   def cari(self, nilai):
      return self.data.index(nilai)
   
   def urutkan(self):
      self.data.sort()
   
   def ekstrak(self, awal, akhir):
      temp = Array(self.data[awal:akhir])
      return temp
   
   def cetak(self):
      for nilai in self.data:
         print(nilai, end=' ')
      print()

def main():
   A = Array([10,20,30,40,50])

   # menampilkan nilai awal
   print("Isi A mula-mula: ", end='')
   A.cetak()

   # mengubah elemen ketiga
   A.ubah(2, 63)

   # menghapus nilai 40
   A.hapus(40)

   # menambah elemen baru
   A.tambah(70)
   A.tambah(15)

   # menampilkan nilai setelah diubah,
   # dihapus, dan ditambah
   print("Isi A setelah dimanipulasi: ", end='')
   A.cetak()

   B = A.ekstrak(1, 4)
   print("Isi B (hasil ekstrak): ", end='')
   B.cetak()

   C = A.salin()
   print("Isi C (salinan A): ", end='')
   C.cetak()

   C.tambah(45.25) # menambah nilai bertipe float

if __name__ == "__main__":
   main()
