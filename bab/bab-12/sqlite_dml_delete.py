######################################################
# Nama file: sqlite_dml_delete.py
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
         # perintah DML untuk menghapus baris data
         # yang kolom KODE-nya bernilai 'P2'
         dml = "DELETE FROM BUKU WHERE KODE='P2'"

         # mengeksekusi statemen DML
         # untuk menghapus baris data di dalam tabel
         cur.execute(dml)
      except:
         print("Error: Penghapusan data gagal dilakukan")
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
