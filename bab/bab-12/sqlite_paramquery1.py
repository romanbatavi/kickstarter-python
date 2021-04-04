######################################################
# Nama file: sqlite_paramquery1.py
######################################################

import sqlite3
import sys

def main():
   penerbit = input("Masukkan nama penerbit: ")

   # inisialisasi objek koneksi
   conn = None

   try:
      # membuat database
      conn = sqlite3.connect("sqlite3db.db")

      # membuat objek cursor
      cur = conn.cursor()

      # menulis query berparameter
      query = """
              SELECT KODE,JUDUL,PENULIS FROM BUKU
              WHERE PENERBIT = ?
              """

      # mengeksekusi query (perintah SELECT)
      cur.execute(query, (penerbit,))

      # menangkap semua baris data
      result = cur.fetchall()

      # menampilkan semua baris data
      for row in result:
         for i in range(len(row)):
            print(row[i], '\t', end='')
         print() # baris baru

   except sqlite3.Error as e:
      print("Error ", e)
   finally:
      if conn:
         # menutup objek koneksi
         conn.close()

if __name__ == "__main__":
   main()
