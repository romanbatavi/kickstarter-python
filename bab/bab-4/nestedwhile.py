######################################################
# Nama file: nestedwhile.py
######################################################

def main():
   i = 1
   while i<=10:
      j=1
      while j<=i:
         print("%d " % (i*j), end='')
         j += 1
      print() # ganti baris
      i += 1

if __name__ == "__main__":
   main()
