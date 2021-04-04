######################################################
# Nama file: nested-whilefor.py
######################################################

def main():
   i = 1
   while i <= 10:
      for j in range(1, i+1):
         print("%d " % (i*j), end='')
      print()
      i += 1

if __name__ == "__main__":
   main()
