######################################################
# Nama file: sqlite_dml_insert.py
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
         data = [
                ("P1", "Expert Python Programming", 
                 "PACKT Publishing", "Tarek Ziade", 2008),
                ("P2", "Python Essential Reference", 
                 "Addison-Wesley", "David M. Beazley", 2009)
                ]
         dml = "INSERT INTO BUKU VALUES(?, ?, ?, ?, ?)"
         # mengeksekusi perintah DML
         # untuk memasukkan data ke dalam tabel
         cur.executemany(dml, data)
      except:
         print("Error: Penambahan data gagal dilakukan")
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
