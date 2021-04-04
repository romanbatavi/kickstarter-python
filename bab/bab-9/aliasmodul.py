######################################################
# Nama file: aliasmodul.py
######################################################

import geometri2D as duaD

def main():
   # persegi panjang
   p = 10 	# panjang
   l = 8	# lebar

   luas = duaD.luasPersegiPanjang(p, l)

   print("PERSEGI PANJANG")
   print("Panjang\t: ", p)
   print("Lebar\t: ", l)
   print("Luas\t= ", luas)

if __name__ == "__main__":
   main()
