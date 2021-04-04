######################################################
# Nama file: if-else2.py
######################################################

def main():
   # membuat tuple
   namahari = ("minggu", "senin", "selasa", "rabu",
               "kamis", "jumat", "sabtu")

   # input untuk tipe data string
   hari = input("Masukkan nama hari: ")

   # perintah if dengan dua ekspresi
   if hari.lower() == namahari[0] or \
      hari.lower() == namahari[6]:
      print(hari + " adalah hari libur")
   else:
      print("%s adalah hari kerja (bagi karyawan)" % hari)

if __name__ == "__main__":
   main()
