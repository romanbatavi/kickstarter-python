######################################################
# Nama file: passbyreference2.py
######################################################

def ubahNilai(alist):
   print("\nDi dalam fungsi")

   alist[0] *= 100  # mengubah indeks pertama

   print("alist[0] = %d" % alist[0])
   return

def main():
   li = [5]  # list dengan 1 anggota

   print("Sebelum pemanggilan fungsi")
   print("li[0] = %d" % li[0])

   # memanggil fungsi ubahNilai()
   # dengan li sebagai parameter aktualnya
   ubahNilai(li)

   print("\nSetelah pemanggilan fungsi")
   print("li[0] = %d" % li[0])

if __name__ == "__main__":
   main()
