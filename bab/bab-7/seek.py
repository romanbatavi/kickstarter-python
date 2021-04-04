######################################################
# Nama file: seek.py
######################################################

def main():
   # membuka file
   f = open("data.txt", "r")

   print("Sebelum file dibaca")
   print("Posisi file: ", f.tell())

   # membaca data sebesar 13 byte
   data1 = f.read(13)

   print("\nSetelah file dibaca 13 byte")
   print("data1: '%s'" % data1)
   print("Posisi file: %d" % f.tell())

   # mengembalikan penunjuk ke posisi 0
   f.seek(0)

   print("\nSetelah dikembalikan ke posisi awal")
   print("Posisi file: ", f.tell())

   # membaca kembali data sebesar 5
   # setelah posisi dipindah ke posisi awal
   data2 = f.read(5)

   print("\nSetelah file dibaca 5 byte")
   print("data2: '%s'" % data2)
   print("Posisi file: %d" % f.tell())

   # menutup file
   f.close()

if __name__ == "__main__":
   main()
