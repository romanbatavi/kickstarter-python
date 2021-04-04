######################################################
# Nama file: maks3bilangan3.py
######################################################

def main():
   # menampilkan judul program
   print("Nilai Maksimum dari Tiga Bilangan")

   # meminta user memasukkan tiga buah bilangan
   a = int(input("\nMasukkan bilangan ke-1: "))
   b = int(input("Masukkan bilangan ke-2: "))
   c = int(input("Masukkan bilangan ke-3: "))

   # menentukan nilai maksimum menggunakan CARA III
   maks = a
   if b > maks: maks = b
   if c > maks: maks = c

   # menampilkan nilai maksimum
   print("\nNilai maksimum adalah %d" % maks)

if __name__ == "__main__":
   main()
