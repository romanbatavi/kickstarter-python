######################################################
# Nama file: dict_get.py
######################################################

def main():
   dict1 = {'satu': 10, 'dua': 20, 'tiga': 30}

   # mencari elemen
   a = dict1.get('satu')
   b = dict1.get('tiga')
   c = dict1.get('enam')

   print("a: ", a)
   print("b: ", b)
   print("c: ", c)

if __name__ == "__main__":
   main()
