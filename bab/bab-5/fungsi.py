######################################################
# Nama file: fungsi.py
######################################################

import os

# mendefinisikan fungsi tanpa nilai balik
def cetak(p):
   "Mencetak teks dan bilangan tanpa baris baru"
   print(p, end='')
   return

# mendefinisikan fungsi dengan nilai balik
def tambahSatu(p):
   "Menambah bilangan p dengan nilai 1"
   value = p + 1
   return value

# mendefinisikan fungsi tanpa nilai balik
# tanpa parameter
def bersihkanLayar():
   "Membersihkan layar"
   os.system("clear")

# mendefinisikan fungsi main() (fungsi utama)
def main():
   # memanggil fungsi bersihkanLayar()
   bersihkanLayar()

   # memanggil fungsi cetak()
   cetak("Umur = ")
   cetak(35)

   print()  # membuat baris baru

   # memanggil fungsi tambahSatu()
   x = tambahSatu(10)
   print("10 + 1 = %d" % x)

if __name__ == "__main__":
   main()   # memanggil fungsi utama
