######################################################
# Nama file: readfor.py
######################################################

def main():
   # membuka file
   f = open("data.txt", "r")

   for baris in f:
      print(baris, end='')

   # menutup file
   f.close()

if __name__ == "__main__":
   main()
