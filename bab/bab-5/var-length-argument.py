######################################################
# Nama file: var-length-argument.py
######################################################

def cetakParameter(*var):
   for i in var:
      print(i)

def main():
   # memanggil fungsi
   print("Satu parameter")
   cetakParameter(10)

   print("\nDua parameter")
   cetakParameter(10, 20)

   print("\nTiga parameter")
   cetakParameter(10, 20, 30)

if __name__ == "__main__":
   main()
