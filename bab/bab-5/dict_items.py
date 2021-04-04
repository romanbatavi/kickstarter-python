######################################################
# Nama file: dict_items.py
######################################################

def main():
   dict1 = {'satu': 10, 'dua': 20, 'tiga': 30}

   a = dict1.items()
   b = dict1.keys()
   c = dict1.values()

   print("\ndict1.items():\n", a)
   print("dict1.keys():\n", b)
   print("dict1.values():\n", c)

if __name__ == "__main__":
   main()
