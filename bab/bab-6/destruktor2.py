######################################################
# Nama file: destruktor2.py
######################################################

# mendefinisikan kelas
class MyFile(object):
   def __init__(self, namafile):
      # mengakses file      
      print("Membuka file %s...\n" % namafile)
      self.file = open(namafile)
   def __del__(self):
      # menutup file
      print("\nMenutup file...")
      self.file.close()      
   def bacadata(self):
      for baris in self.file:
         print(baris, end="")

def main():
   # membuat objek dari kelas MyFile
   f = MyFile("D:\\kodepython\\sample.txt")
   #f = MyFile("sample.txt")

   # memanggil metode bacadata()
   f.bacadata()

if __name__ == "__main__":
   main()
