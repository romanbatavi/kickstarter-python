######################################################
# Nama file: mysql_dml_insert.py
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

      data1 = ("P1", 
              "Expert Python Programming", 
              "PACKT Publishing", 
              "Tarek Ziade", 
              2008)

      data2 = ("P2", 
              "Python Essential Reference", 
              "Addison-Wesley", 
              "David M. Beazley", 
              2009)

      sql = """
            INSERT INTO BUKU VALUES
            (%s, %s, %s, %s, %s)
            """
      try:
         cur.execute(sql, data1)
         cur.execute(sql, data2)
      except mysql.connector.DataError:
         # melakukan rollback data
         conn.rollback()
         print("Data gagal disimpan")
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
