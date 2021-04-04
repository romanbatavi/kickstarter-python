######################################################
# Nama file: dict-selection2.py
######################################################

# mendefinisikan fungsi tambah()
def tambah(a, b):
   return a + b

# mendefinisikan fungsi kurang()
def kurang(a, b):
   return a - b

# mendefinisikan fungsi kali()
def kali(a, b):
   return a * b

# mendefinisikan fungsi bagi()
def bagi(a, b):
   return a / b

def main():
   a = float(input("Masukkan bilangan ke-1\t: "))
   b = float(input("Masukkan bilangan ke-2\t: "))
   op = input("Masukkan operator\t: ")

   # membuat dictionary yang nilainya berupa fungsi
   d = {
         '+': tambah(a, b),
         '-': kurang(a, b),
         '*': kali(a, b),
         'x': kali(a, b),
         '/': bagi(a, b),
         ':': bagi(a, b)
       }

   print("\n%f %s %f = %f" % (a, op, b, d[op]))

if __name__ == "__main__":
   main()
