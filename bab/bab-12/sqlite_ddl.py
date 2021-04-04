######################################################
# Nama file: sqlite_ddl.py
######################################################

# mengimpor modul sqlite3
import sqlite3
import sys

def main():
   # inisialisasi objek koneksi
   conn = None

   try:
      # membuat database
      conn = sqlite3.connect("sqlite3db.db")
      # membuat objek cursor
      cur = conn.cursor()
      try:
         ddl = """
               CREATE TABLE BUKU (
                  KODE CHAR(2) NOT NULL PRIMARY KEY,
                  JUDUL VARCHAR(50),
                  PENERBIT VARCHAR(30),
                  PENULIS VARCHAR(25),
                  TAHUN INTEGER
               )
               """
         # mengeksekusi statemen DDL
         # untuk membuat tabel
         cur.execute(ddl)
      except:
         print("Error: Tabel tidak dapat dibuat")
         sys.exit(1)
      else:
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
