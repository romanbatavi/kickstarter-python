######################################################
# Nama file: if1.py
######################################################

def main():
   bilangan = int(input("Masukkan bilangan bulat: "))

   # memeriksa bilangan, genap atau tidak
   if bilangan % 2 == 0:
      print("%d adalah bilangan genap" % bilangan)

if __name__ == "__main__":
   main()
