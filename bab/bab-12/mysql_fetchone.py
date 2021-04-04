######################################################
# Nama file: mysql_fetchone.py
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
         cur = conn.cursor(buffered=True)
         cur.execute(sql)

         # menangkap satu baris data dalam cursor
         row = cur.fetchone()

         print("Menggunakan fetchone():")
         # menampilkan data yang telah ditangkap
         print(row[0], '\t', 
               row[1], '\t', 
               row[2])
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
