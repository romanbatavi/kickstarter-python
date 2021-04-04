######################################################
# Nama file: forelse.py
######################################################

def main():
   for i in range(10, 25):
      # pengulangan menggunakan for..else
      for j in range(2, i):
         if i % j == 0:
            print("%d bukan prima" % i)
            break
      else:
         print("%d adalah bilangan prima" % i)

if __name__ == "__main__":
   main()
