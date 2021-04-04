######################################################
# Nama file: tell.py
######################################################

def main():
   # membuka file
   f = open("data.txt", "r")

   print("Sebelum file dibaca")
   print("Posisi file: %d" % f.tell())

   # membaca data sebesar 13 byte
   data1 = f.read(13)

   print("\nSetelah file dibaca 13 byte")
   print("data1: '%s'" % data1)
   print("Posisi file: %d" % f.tell())

   # membaca kembali data sebesar 7
   data2 = f.read(7)

   print("\nSetelah file dibaca 7 byte")
   print("data2: '%s'" % data2)
   print("Posisi file: %d" % f.tell())

   # menutup file
   f.close()

if __name__ == "__main__":
   main()
