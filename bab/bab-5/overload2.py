######################################################
# Nama file: overload2.py
######################################################

# mendefinisikan fungsi jumlah()
def jumlah(*bil):
   hasil = 0
   for i in bil:
      hasil += i
   return hasil

def main():
   # memanggil fungsi jumlah()
   print("jumlah(2, 3) \t\t= ", jumlah(2, 3))
   print("jumlah(2, 3, 4) \t= ", jumlah(2, 3, 4))

if __name__ == "__main__":
   main()
