######################################################
# Nama file: input-integer1.py
######################################################

def main():
   # membuat prompt untuk tipe data string
   s = input("Masukkan bilangan bulat: ")

   # melakukan konversi dari string ke tipe integer
   bilbulat = int(s)

   # menggunakan variabel untuk melakukan perhitungan
   hasil = bilbulat + 1

   # menampilkan nilai variabel
   print("Bilangan yang dimasukkan adalah %d" % bilbulat)
   print("%d + 1 = %d" % (bilbulat, hasil))

if __name__ == "__main__":
   main()
