######################################################
# Nama file: maks2bilangan.py
######################################################

def main():
   # menampilkan judul program
   print("Nilai Maksimum dari Dua Bilangan")

   # meminta user memasukkan dua buah bilangan
   a = int(input("\nMasukkan bilangan ke-1: "))
   b = int(input("Masukkan bilangan ke-2: "))

   # menentukan nilai maksimum
   if a > b:
      maks = a
   else:
      maks = b

   # menampilkan nilai maksimum
   print("\nNilai maksimum adalah %d" % maks)

if __name__ == "__main__":
   main()
