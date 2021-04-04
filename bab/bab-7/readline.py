######################################################
# Nama file: readline.py
######################################################

def main():
   # membuka file
   f = open("data.txt", "r")

   # membaca data tiap baris
   while True:
      baris = f.readline()
      if not baris:  # EOF (end of file)
         break
      print(baris, end='')

   # menutup file
   f.close()

if __name__ == "__main__":
   main()
