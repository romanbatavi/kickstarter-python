######################################################
# Nama file: sqlite_dml_update.py
######################################################

import sqlite3
import sys

def main():
   # inisialisasi objek koneksi
   conn = None

   try:
      # membuka database
      conn = sqlite3.connect("sqlite3db.db")
      # membuat objek cursor
      cur = conn.cursor()
      try:
         # perintah DML untuk mengubah kolom TAHUN menjadi 2013
         # pada baris data yang kolom KODE-nya bernilai 'P1'
         dml = "UPDATE BUKU SET TAHUN=2013 WHERE KODE='P1'"

         # mengeksekusi statemen DML
         # untuk mengubah baris data di dalam tabel
         cur.execute(dml)
      except:
         print("Error: Perubahan data gagal dilakukan")
         conn.rollback()
         sys.exit(1)
      else:
         # melakukan commit data
         conn.commit()
         # menutup objek cursor
         cur.close()
   except sqlite3.Error as e:
      print("Error ", e)
   finally:
      if conn:
         # menutup objek koneksi
         conn.close()

if __name__ == "__main__":
   main()
