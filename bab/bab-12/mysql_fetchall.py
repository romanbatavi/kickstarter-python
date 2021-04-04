######################################################
# Nama file: mysql_fetchall.py
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
         for row in result:
            kode = row[0]    # kolom ke-1 result set
            judul = row[1]   # kolom ke-2 result set
            penulis = row[2] # kolom ke-3 result set
            # menampilkan ke layar
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
