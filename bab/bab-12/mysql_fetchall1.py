######################################################
# Nama file: mysql_fetchall1.py
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
            """
      try:
         cur = conn.cursor()
         cur.execute(sql)

         # menangkap semua data dalam cursor
         result = cur.fetchall()

         # mengekstrak data tiap baris
         for (kode,judul,penulis) in result:
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
