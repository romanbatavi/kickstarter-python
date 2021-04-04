######################################################
# Nama file: if-else1.py
######################################################

def main():
   # input untuk tipe integer
   bilangan = int(input("Masukkan bilangan bulat: "))

   # membuat bilangan, genap atau ganjil
   if bilangan % 2 == 0:
      print("%d adalah bilangan genap" % bilangan)
   else:
      print("%d adalah bilangan ganjil" % bilangan)

if __name__ == "__main__":
   main()
