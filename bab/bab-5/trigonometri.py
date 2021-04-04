######################################################
# Nama file: trigonometri.py
######################################################

import math

def main():
   sudut = 90  # dalam derajat

   y = math.sin(math.radians(sudut))	# sin 90
   x =  math.degrees(math.asin(y))	# arcsin 1

   # menampilkan nilai sinus 90
   print("sin 90 \t\t: ", y)
   print("arcsin 1 \t: ", x)

if __name__ == "__main__":
   main()
