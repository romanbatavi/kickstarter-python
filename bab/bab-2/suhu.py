######################################################
# Nama file: suhu.py
######################################################

def main():
   # menampilkan informasi program
   print("Konversi Suhu (Fahrenheit ke Celcius)\n")

   # input suhu dalam Fahrenheit
   F = float(input("Masukkan suhu (Fahrenheit): "))

   # melakukan konversi suhu ke Celcius
   C = 5 * (F - 32) / 9

   # menampilkan hasil konversi ke layar
   print("Fahrenheit \t:", F)
   print("Celcius \t:", C)

if __name__ == "__main__":
   main()
