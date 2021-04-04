######################################################
# Nama file: aliasfungsi.py
######################################################

from geometri2D import luasLingkaran as llk

def main():
   # lingkaran
   jarijari = 3

   luas = llk(jarijari)

   print("LINGKARAN")
   print("Jari-jari\t: ", jarijari)
   print("Luas\t= ", luas)

if __name__ == "__main__":
   main()
