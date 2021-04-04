######################################################
# Nama file: exit.py
######################################################

import sys	# untuk menggunakan fungsi exit()

def main():
   print("Program pembagian bilangan")
   a = float(input("\nMasukkan nilai a: "))
   b = float(input("Masukkan nilai b: "))
   
   if b == 0.0:
      print("Kesalahan: Nilai b tidak boleh nol")
      sys.exit(1)

   c = a / b

   print("%.2f / %.2f = %.2f" % (a, b, c))

if __name__ == "__main__":
   main()
