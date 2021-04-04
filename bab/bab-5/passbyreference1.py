######################################################
# Nama file: passbyreference1.py
######################################################

def ubahNilai(p):
   print("\nDi dalam fungsi")
   print("p lama \t\t= %d" % p) # p lama
   print("ID p lama \t= %d" % id(p))

   p *= 100  # membuat objek p baru

   print("\np baru \t\t= %d" % p) # p baru
   print("ID p baru \t= %d" % id(p))   
   return

def main():
   a = 5

   print("Sebelum pemanggilan fungsi")
   print("a \t\t= %d" % a)
   print("ID a \t\t= %d" % id(a))

   # memanggil fungsi ubahNilai()
   # dengan a sebagai parameter aktualnya
   ubahNilai(a)

   print("\nSetelah pemanggilan fungsi")
   print("a \t\t= %d" % a)
   print("ID a \t\t= %d" % id(a))

if __name__ == "__main__":
   main()
