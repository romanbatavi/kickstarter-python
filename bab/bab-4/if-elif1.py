######################################################
# Nama file: if-elif1.py
######################################################

def main():
   x = int(input("Masukkan bilangan bulat: "))

   # memeriksa nilai x
   if x > 0:
      print("%d adalah bilangan positif" % x)
   elif x == 0:
      print("Anda memasukkan nilai nol" % x)
   else:
      print("%d adalah bilangan negatif" % x)


if __name__ == "__main__":
   main()
