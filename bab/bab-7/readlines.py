######################################################
# Nama file: readlines.py
######################################################

def main():
   # membuka file
   f = open("data.txt", "r")

   # membaca seluruh baris, dan menampungnya
   # ke dalam objek list
   data = f.readlines()

   print(data)

   # menutup file
   f.close()

if __name__ == "__main__":
   main()
