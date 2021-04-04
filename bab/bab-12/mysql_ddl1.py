######################################################
# Nama file: mysql_ddl1.py
######################################################

# mengimpor modul mysql.connector
import mysql.connector
import sys

def main():
   try:
      # membuat objek koneksi
      conn = mysql.connector.connect(
         user="raharjo", 
         password="123456789", 
         host="127.0.0.1", 
         database="PythonDB" 
      )

      # membuat objek cursor
      cur = conn.cursor()

      ddl = """
            CREATE TABLE BUKU (
               KODE CHAR(2) NOT NULL PRIMARY KEY,
               JUDUL VARCHAR(50),
               PENERBIT VARCHAR(30),
               PENULIS VARCHAR(25),
               TAHUN INTEGER
            )
            """

      # mengeksekusi statemen SQL
      # untuk membuat tabel BUKU
      cur.execute(ddl)
      # menutup objek cursor
      cur.close()
   except mysql.connector.Error as e:
      print("ERROR ", e)   
   else:
      print("Tabel BUKU sukses dibuat...")
      # menutup objek cursor dan koneksi
      conn.close()

if __name__ == "__main__":
   main()
