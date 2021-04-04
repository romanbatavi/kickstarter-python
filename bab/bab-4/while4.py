######################################################
# Nama file: while4.py
######################################################

def main():
   # melakukan pengulangan dari indeks 'a' sampai 'e'
   ch = 'a'
   while ch <= 'e':
      print("%c: Hello World!" % ch)
      ch = chr(ord(ch) + 1)

if __name__ == "__main__":
   main()
