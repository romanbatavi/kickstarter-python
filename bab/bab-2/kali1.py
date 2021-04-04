######################################################
# Nama file: kali1.py
######################################################

def main():
   # menampilkan judul program
   print("Perkalian Bilangan dengan Operator +")

   # meminta user memasukkan bilangan 
   a = int(input("\nMasukkan bilangan ke-1: "))
   b = int(input("Masukkan bilangan ke-2: "))

   # menghitung perkalian bilangan
   hasilkali = 0
   for i in range(0, abs(b)):
      if b < 0:
         hasilkali -= a
      else:
         hasilkali += a

   # menampilkan hasil
   print("\n%d x %d = %d" % (a, b, hasilkali))

if __name__ == "__main__":
   main()
