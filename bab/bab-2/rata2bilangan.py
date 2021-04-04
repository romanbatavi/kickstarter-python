######################################################
# Nama file: rata2bilangan.py
######################################################

def main():
   # menampilkan judul program
   print("Rata-rata Bilangan")

   # menyiapkan list untuk menampung data
   data = []  # data mula-mula kosong

   # meminta user memasukkan banyaknya data
   n = int(input("\nMasukkan banyak data: "))

   print() # membuat spasi baris

   jumlah = 0
   for i in range(0, n):
     # meminta user mengisi data bilangan
     temp = int(input("Masukkan data ke-%d: " % (i+1)))
     
     # menambahkan bilangan ke dalam list
     data.append(temp)

     # menghitung jumlah total bilangan
     jumlah += data[i]

   # menghitung rata-rata
   rata2 = jumlah / n

   # menampilkan hasil
   print("\nRata-rata  = %0.2f" % rata2)

if __name__ == "__main__":
   main()
