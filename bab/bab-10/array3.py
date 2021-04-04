######################################################
# Nama file: array3.py
######################################################

import sys

# mendefinisikan array asosiatif
KAMUS = {
          'one':'satu',
          'two':'dua',
          'three':'tiga',
          'four':'empat',
          'five':'lima',
          'six':'enam',
          'seven':'tujuh',
          'eight':'delapan',
          'nine':'sembilan',
          'ten':'sepuluh'
          # ...
        }

def main():
   # meminta user memasukkan kata dalam bahasa inggris
   kata = input("Masukkan kata dalam bahasa inggris: ")

   if not (kata in KAMUS.keys()):
      print("'%s' tidak ditemukan di dalam kamus ini" % kata)
      sys.exit(1)

   print("Arti kata '%s' adalah '%s'" % (kata, KAMUS[kata]))

if __name__ == "__main__":
   main()
