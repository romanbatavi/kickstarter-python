######################################################
# Nama file: indeksujian.py
######################################################

def main():
   # menampilkan judul program
   print("Nilai Indeks Mahasiswa")

   # meminta user memasukkan nilai UTS dan UAS
   uts = float(input("\nMasukkan nilai UTS: "))
   uas = float(input("Masukkan nilai UAS: "))

   # menghitung nilai akhir
   na = (0.65 * uas) + (0.35 * uts)

   # menentukan nilai indeks
   if na >= 80:
      indeks = 'A'
   elif na >= 70:
      indeks = 'B'
   elif na >= 55:
      indeks = 'C'
   elif na >= 40:
      indeks = 'D'
   else:
      indeks = 'E'

   # menampilkan hasil
   print("\nNilai Akhir  = %0.2f" % na)
   print("Nilai Indeks = %c" % indeks)

if __name__ == "__main__":
   main()
