######################################################
# Nama file: maks3bilangan1.py
######################################################

def main():
   # menampilkan judul program
   print("Nilai Maksimum dari Tiga Bilangan")

   # meminta user memasukkan tiga buah bilangan
   a = int(input("\nMasukkan bilangan ke-1: "))
   b = int(input("Masukkan bilangan ke-2: "))
   c = int(input("Masukkan bilangan ke-3: "))

   # menentukan nilai maksimum menggunakan CARA I
   if a > b:
      if a > c:
         maks = a
   else:
      if b > c:
         maks = b
      else:
         maks = c

   # menampilkan nilai maksimum
   print("\nNilai maksimum adalah %d" % maks)

if __name__ == "__main__":
   main()
