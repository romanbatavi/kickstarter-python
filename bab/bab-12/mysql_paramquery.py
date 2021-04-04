######################################################
# Nama file: mysql_paramquery.py
######################################################

import mysql.connector
import sys

def main():
   try:
      conn = mysql.connector.connect(
         user="raharjo", 
         password="123456789", 
         host="127.0.0.1", 
         database="PythonDB" 
      )
   
      sql = """
            SELECT KODE, JUDUL, PENULIS
            FROM BUKU
            WHERE KODE = %(kodebuku)s
            """
      try:
         cur = conn.cursor()
         # mengeksekusi SQL dengan parameter
         cur.execute(sql, { 'kodebuku': 'P2' })
         # menampilkan data
         for (kode,judul,penulis) in cur:
            print(kode, '\t', 
                  judul, '\t', 
                  penulis)
      except:
         print("Pengambilan data gagal")
         sys.exit(1)
      else:
         cur.close()
   
   except mysql.connector.Error as e:
      print("ERROR ", e)
   else:
      conn.close()

if __name__ == "__main__":
   main()
