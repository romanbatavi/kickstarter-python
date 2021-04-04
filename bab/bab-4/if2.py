######################################################
# Nama file: if2.py
######################################################

def main():
   # membuat tuple
   namahari = ("minggu", "senin", "selasa", "rabu",
               "kamis", "jumat", "sabtu")

   # membuat prompt untuk input tipe data string
   hari = input("Masukkan nama hari: ")

   # perintah if dengan dua ekspresi
   if hari.lower() == namahari[0] or \
      hari.lower() == namahari[6]:
      print("%s adalah hari libur" % hari)

if __name__ == "__main__":
   main()
