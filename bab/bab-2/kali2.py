######################################################
# Nama file: kali2.py
######################################################

def main():
   # menampilkan judul program
   print("Perkalian Bilangan dengan Operator +")

   # meminta user memasukkan bilangan 
   a = int(input("\nMasukkan bilangan ke-1: "))
   b = int(input("Masukkan bilangan ke-2: "))

   # menghitung perkalian bilangan
   hasilkali = 0
   for i in range(0, abs(a)):
      if a < 0:
         hasilkali -= b
      else:
         hasilkali += b


   # menampilkan hasil
   print("\n%d x %d = %d" % (a, b, hasilkali))

if __name__ == "__main__":
   main()
