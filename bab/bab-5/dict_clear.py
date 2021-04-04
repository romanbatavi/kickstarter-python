######################################################
# Nama file: dict_clear.py
######################################################

def main():
   dict1 = {'satu': 10, 'dua': 20, 'tiga': 30}
   dict2 = {'satu': 10, 'dua': 20}

   print("dict1: ", dict1)
   print("dict2: ", dict2)

   print("\nlen(dict1): ", len(dict1))
   print("len(dict2): ", len(dict2))

   # mengosongkan elemen
   dict1.clear()
   dict2.clear()

   # menampilkan jumlah elemen
   # setelah dikosongkan
   print("\nSetelah semua elemen dihapus")
   print("len(dict1): ", len(dict1))
   print("len(dict2): ", len(dict2))

if __name__ == "__main__":
   main()
