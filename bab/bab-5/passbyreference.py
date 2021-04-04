######################################################
# Nama file: passbyreference.py
######################################################

def ubahNilai(p):
   p *= 100
   print("\nNilai di dalam fungsi")
   print("p = %d" % p)
   return 

def main():
   a = 5

   print("Sebelum pemanggilan fungsi")
   print("a = %d" % a)

   # memanggil fungsi ubahNilai()
   # dengan a sebagai parameter aktualnya
   ubahNilai(a)

   print("\nSetelah pemanggilan fungsi")
   print("a = %d" % a)

if __name__ == "__main__":
   main()
