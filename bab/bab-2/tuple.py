######################################################
# Nama file: tuple.py
######################################################

import datetime as dt

def main():
   # tuple untuk nama bulan
   BULAN = ("Januari","Februari","Maret",
            "April","Mei","Juni",
            "Juli","Agustus","September",
            "Oktober","November","Desember")

   # today akan berisi: 'YYYY-MM-DD'
   today = dt.date.isoformat(dt.date.today())

   yyyy = today[:4]
   mm = today[5:7]
   dd = today[8:]

   print(today)
   print("%s %s %s" % (dd, BULAN[int(mm)-1], yyyy))

if __name__ == "__main__":
   main()
