######################################################
# Nama file: keywordargument.py
######################################################

def infoKaryawan(nama, usia, gaji):
   print("Nama: %s" % nama)
   print("Usia: %d" % usia)
   print("Gaji: %d" % gaji, end="\n\n")

def main():
   # memanggil fungsi
   infoKaryawan(nama="Bimo", usia=35, gaji=6000000)
   infoKaryawan(usia=36, nama="Sakti", gaji=5000000)
   infoKaryawan(gaji=7000000, usia=37, nama="Dewa")

if __name__ == "__main__":
   main()
