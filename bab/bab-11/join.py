######################################################
# Nama file: join.py
######################################################

import os

def main():
   os.chdir("E:\\kodepython")

   # data dalam bentuk list
   data = [
            ["101", "Dewi Puspita", "08122299999"],
            ["102", "Ahmad Dahlan", "08152288888"],
            ["103", "Ponco Wibowo", "08562277777"],
            ["104", "Roro Minarsih", "08122666666"]
          ]

   # menulis data ke dalam file
   f = open("data.csv", "w+")
   for baris in data:
      f.write(";".join(baris) + "\n")
	
   f.close()

   # menampilkan isi file
   f = open("data.csv")
   for baris in f:
      print(baris, end='')

if __name__ == "__main__":
   main()
