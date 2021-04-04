######################################################
# Nama file: rekursi.py
######################################################

import sys

# mendefinisikan fungsi rekursif
def faktorial(n):
   if n==0:
      return 1
   else:
      return n * faktorial(n-1)

def main():
   bil = int(input("Masukkan bilangan yang akan dihitung: "))

   if bil < 0:
      print("ERROR: Bilangan tidak boleh negatif")
      sys.exit(1)

   print("%d! = %d" % (bil, faktorial(bil)))

if __name__ == "__main__":
   main()
