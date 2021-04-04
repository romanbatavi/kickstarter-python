######################################################
# Nama file: paket.py
######################################################

# mengimpor modul geometri2D
# yang berada di dalam paket Matematika
import Matematika.geometri2D

def main():
   # bujursangkar
   sisi = 5

   luas = Matematika.geometri2D.luasBujursangkar(sisi)

   print("BUJURSANGKAR")
   print("Panjang sisi\t: ", sisi)
   print("Luas\t\t= ", luas)

if __name__ == "__main__":
   main()
