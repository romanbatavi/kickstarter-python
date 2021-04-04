######################################################
# Nama file: defaultparameter.py
######################################################

# mendefinisikan fungsi dengan parameter default
def infoKaryawan(nama, usia=35):
   print("Nama: %s" % nama)
   print("Usia: %d" % usia, end="\n\n")
   return

def main():
   # memanggil fungsi infoKaryawan()
   infoKaryawan("Bimo")
   infoKaryawan("Haryo", 33)
   infoKaryawan("Hanggoro", 37)

if __name__ == "__main__":
   main()
