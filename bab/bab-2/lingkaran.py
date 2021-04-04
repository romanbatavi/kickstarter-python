######################################################
# Nama file: lingkaran.py
######################################################

import math

def main():
   # menampilkan informasi program
   print("Luas dan Keliling Lingkaran\n")

   # input nilai jari-jari
   r = float(input("Masukkan nilai jari-jari: "))

   # menghitung luas lingkaran
   L = math.pi * (r ** 2)

   # menghitung keliling lingkaran
   K = 2 * math.pi * r

   # menampilkan hasil perhitungan ke layar
   print("Luas \t\t:", L)
   print("Keliling \t: ", K)

if __name__ == "__main__":
   main()
