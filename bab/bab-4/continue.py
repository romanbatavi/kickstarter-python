######################################################
# Nama file: continue.py
######################################################

def main():
   for i in range(1,11):
      if i % 2 == 0:
         continue	# melanjutkan pengulangan untuk i berikutnya

      # baris di bawah ini hanya akan dieksekusi 
      # jika i bernilai ganjil
      print(i, end='\t')

if __name__ == "__main__":
   main()
