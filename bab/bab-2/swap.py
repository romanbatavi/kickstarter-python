######################################################
# Nama file: swap.py
######################################################

def main():
   # menampilkan informasi program
   print("Menukar Nilai dari Dua Variabel\n")

   # input variabel ke-1 dan ke-2
   a = int(input("Masukkan variabel ke-1: "))
   b = int(input("Masukkan variabel ke-2: "))

   # menampilkan nilai sebelum ditukar
   print("\nSebelum pertukaran nilai")
   print("Variabel ke-1 \t:", a)
   print("Variabel ke-2 \t:", b)

   # melakukan pertukaran nilai
   c = a  # c adalah variabel bantu
   a = b
   b = c

   # menampilkan nilai setelah ditukar
   print("\nSetelah pertukaran nilai")
   print("Variabel ke-1 \t:", a)
   print("Variabel ke-2 \t:", b)

if __name__ == "__main__":
   main()
