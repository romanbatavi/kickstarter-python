######################################################
# Nama file: fromimport.py
######################################################

# mengimpor fungsi luasPersegiPanjang
# dari modul geometri2D
from geometri2D import luasPersegiPanjang

def main():
   # persegi panjang
   p = 10 	# panjang
   l = 8	# lebar

   luas = luasPersegiPanjang(p, l)

   print("PERSEGI PANJANG")
   print("Panjang\t: ", p)
   print("Lebar\t: ", l)
   print("Luas\t= ", luas)

if __name__ == "__main__":
   main()
