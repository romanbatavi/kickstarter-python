######################################################
# Nama file: choice.py
######################################################

import random

def main():
   li = [10, 20, 30, 40, 50]

   print("li: ", li)

   print("\nPemanggilan pertama")
   print("random.choice(li): ", random.choice(li))

   print("\nPemanggilan kedua")
   print("random.choice(li): ", random.choice(li))

   print("\nPemanggilan ketiga")
   print("random.choice(li): ", random.choice(li))

if __name__ == "__main__":
   main()
