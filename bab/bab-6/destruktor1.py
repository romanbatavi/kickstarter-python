######################################################
# Nama file: destruktor1.py
######################################################

# mendefinisikan kelas
class MyFile(object):
   def __init__(self, namafile):
      # mengakses file      
      self.file = open(namafile)
   def __del__(self):
      # menutup file
      self.file.close()      
   def bacadata(self):
      for baris in self.file:
         print(baris, end="")

def main():
   # membuat objek dari kelas MyFile
   f = MyFile("E:\\kodepython\\sample.txt")
   #f = MyFile("sample.txt")	# jika file berada dalam satu direktori

   # memanggil metode bacadata()
   f.bacadata()

if __name__ == "__main__":
   main()
