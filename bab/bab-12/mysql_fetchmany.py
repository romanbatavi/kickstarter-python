######################################################
# Nama file: mysql_fetchmany.py
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
         rows = cur.fetchmany(2)

         print("Menggunakan fetchmany(2):")
         # menampilkan data yang telah ditangkap
         for (kode,judul,penulis) in rows:
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
