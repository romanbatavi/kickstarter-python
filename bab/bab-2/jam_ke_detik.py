######################################################
# Nama file: jam_ke_detik.py
######################################################

def main():
   # menampilkan informasi program
   print("Konversi Jam ke Detik\n")

   # input jam, menit, dan detik
   hh = int(input("Masukkan jumlah jam \t: "))
   mm = int(input("Masukkan jumlah menit \t: "))
   ss = int(input("Masukkan jumlah detik \t: "))

   # melakukan konversi hh:mm:ss ke detik
   totaldetik = (hh * 3600) + (mm * 60) + ss

   # menampilkan hasil konversi
   print(str(hh) + ':' + str(mm) + ':' + str(ss) + 
         " sama dengan " + str(totaldetik) + 
         " detik")

if __name__ == "__main__":
   main()
