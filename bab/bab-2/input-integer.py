######################################################
# Nama file: input-integer.py
######################################################

def main():
   # membuat prompt untuk tipe data integer
   bilbulat = input("Masukkan bilangan bulat: ")

   # menggunakan variabel untuk melakukan perhitungan
   hasil = bilbulat + 1

   # menampilkan nilai variabel
   print("Bilangan yang dimasukkan adalah %d" % bilbulat)
   print("%d + 1 = %d" % (bilbulat, hasil))

if __name__ == "__main__":
   main()
