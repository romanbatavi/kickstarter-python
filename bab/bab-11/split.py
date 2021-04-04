######################################################
# Nama file: split.py
######################################################

import os

def main():
   f = open("data.csv")
   data = []
   for baris in f:
      barisdata = baris.split(';')
      data.append(barisdata)
	
   f.close()

   # menampilkan elemen di dalam list data
   for baris in data:
      print("%s\t%s\t%s" % (baris[0], baris[1], baris[2]), end='')

if __name__ == "__main__":
   main()
