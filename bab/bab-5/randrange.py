######################################################
# Nama file: randrange.py
######################################################

import random

def main():
   # mengambil nilai acak dari 1 sampai 100
   print("random.randrange(1, 100): ", 
          random.randrange(1, 100))

   # mengambil nilai acak dari 1 sampai 1000
   print("random.randrange(1, 1000): ", 
          random.randrange(1, 1000))

   # mengambil nilai acak dari -100 sampai 0
   print("random.randrange(-100, 0): ", 
          random.randrange(-100, 0))

if __name__ == "__main__":
   main()
