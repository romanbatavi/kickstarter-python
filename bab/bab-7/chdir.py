######################################################
# Nama file: chdir.py
######################################################

# mengimpor modul os
import os

def main():
   # mendapatkan informasi tentang direktori aktif
   s = os.getcwd()

   print("Direktori aktif: ", s)

   # mengubah direktori aktif
   # ke C:\Python37
   os.chdir("C:\\Python37")

   s1 = os.getcwd()

   print("\nSetelah direktori aktif diubah")
   print("Direktori aktif: ", s1)

if __name__ == "__main__":
   main()
