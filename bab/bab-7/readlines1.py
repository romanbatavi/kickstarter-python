######################################################
# Nama file: readlines1.py
######################################################

def main():
   # membuka file
   f = open("data.txt", "r")

   data = f.readlines()

   # mengambil elemen dari list
   for elemen in data:
      print(elemen, end='')

   # menutup file
   f.close()

if __name__ == "__main__":
   main()
