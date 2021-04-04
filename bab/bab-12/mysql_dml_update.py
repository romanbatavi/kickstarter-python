######################################################
# Nama file: mysql_dml_update.py
######################################################

# mengimpor modul mysql.connector
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

      cur = conn.cursor()

      sql = """
            UPDATE BUKU
              SET TAHUN = 2013
            WHERE
              KODE = 'P1'
            """
      try:
         cur.execute(sql)
      except mysql.connector.DataError:
         # melakukan rollback data
         conn.rollback()
         print("Data gagal diubah")
         sys.exit(1)
      else:
         # melakukan commit data
         conn.commit()
         cur.close()

   except mysql.connector.Error as e:
      print("ERROR ", e)
   else:
      conn.close()

if __name__ == "__main__":
   main()
