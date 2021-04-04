######################################################
# Nama file: dict_fromkeys.py
######################################################

def main():
   # mendefinisikan tuple t
   t = ('satu', 'dua', 'tiga')

   # membuat dictionary
   dict1 = dict.fromkeys(t, 40)

   print("dict1: ", dict1)

if __name__ == "__main__":
   main()
