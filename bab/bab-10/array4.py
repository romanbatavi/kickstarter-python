######################################################
# Nama file: array4.py
######################################################

# mendefinisikan array dua dimensi
A  = [
        [23,11,54,38,76],
        [14,12,20,22,21],
        [10,13,18,17,24],
        [35,33,39,32,29]
     ]

BARIS = 4
KOLOM = 5

def main():
   print("Isi array A:")
   # menampilkan elemen array dua dimensi
   i = 0;
   while i < BARIS:
      j = 0
      while j < KOLOM:
         print("%d " % A[i][j], end='')
         j += 1
      i += 1
      print()	# ganti baris

if __name__ == "__main__":
   main()
