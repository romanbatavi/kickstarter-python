######################################################
# Nama file: return.py
######################################################

# mendefinisikan fungsi
def tambah(a, b):
   c = a + b
   return c  # akan mengembalikan eksekusi ke baris pemanggil

def main():
   x = int(input("Masukkan bilangan ke-1: "))
   y = int(input("Masukkan bilangan ke-2: "))

   hasil = tambah(x, y)  # baris pemanggil

   print("%d + %d = %d" % (x, y, hasil))

if __name__ == "__main__":
   main()
