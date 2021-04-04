######################################################
# Nama file: sqlite_autocommit.py
######################################################

import sqlite3
import sys

def main():
   # inisialisasi objek koneksi
   conn = None

   try:
      # membuka database
      conn = sqlite3.connect("sqlite3db.db", isolation_level=None)
      # membuat objek cursor
      cur = conn.cursor()
      try:
         data = [
                ("P3", "CherryPy Essentials", 
                 "PACKT Publishing", "Sylvain Hellegourach", 2007),
                ("P4", "Core Python Programming", 
                 "Prentice Hall", "Wesley J. Chun", 2006),
                ("P5", "Python 2.1 Bible", 
                 "Hungry Minds", "Dave Brueck & Stephen T.", 2001)
                ]
         dml = "INSERT INTO BUKU VALUES(?, ?, ?, ?, ?)"
         cur.executemany(dml, data)
      except:
         print("Error: Penambahan data gagal dilakukan")
         sys.exit(1)
      else:
         # conn.commit()	# baris ini tidak perlu ditulis lagi
         cur.close()
   except sqlite3.Error as e:
      print("Error ", e)
   finally:
      if conn:
         # menutup objek koneksi
         conn.close()

if __name__ == "__main__":
   main()
