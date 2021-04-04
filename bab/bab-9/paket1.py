######################################################
# Nama file: paket1.py
######################################################

from Matematika.geometri2D import luasBujursangkar

def main():
   # bujursangkar
   sisi = 5

   luas = luasBujursangkar(sisi)

   print("BUJURSANGKAR")
   print("Panjang sisi\t: ", sisi)
   print("Luas\t\t= ", luas)

if __name__ == "__main__":
   main()
