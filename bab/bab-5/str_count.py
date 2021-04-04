######################################################
# Nama file: str_count.py
######################################################

def main():
   str = "hello world!"
   a = str.count('l')
   b = str.count('o')
   c = str.count('l', 1, 6)

   print("Huruf 'l' dalam str: ", a)
   print("Huruf 'o' dalam str: ", b)
   print("Huruf 'l' dari indeks 1-6: ", c)

if __name__ == "__main__":
   main()
