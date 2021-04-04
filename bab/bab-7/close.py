######################################################
# Nama file: close.py
######################################################

def main():
   # membuka file
   f = open("data.txt")

   # menggunakan file
   print("Nama file\t: ", f.name)
   print("Tertutup?\t: ", f.closed)
   print("Mode akses\t: ", f.mode)

   # menutup file
   f.close()

   print("\nSetelah ditutup")
   print("Tertutup?\t: ", f.closed)

if __name__ == "__main__":
   main()
