######################################################
# Nama file: relasional.py
######################################################

def main():
   # mendefinisikan variabel x, y, 
   # dan li (bertipe list)
   x = 4
   y = 5
   li = [5, 10, 15, 20, 25]

   # menampilkan nilai x dan y
   print("x =", x)
   print("y =", y)
   print(li)

   # melakukan pemeriksaan terhadap x dan y
   print("x == y \t:", (x == y))
   print("x != y \t:", (x != y))
   print("x > y \t:", (x > y))
   print("x >= y \t:", (x >= y))
   print("x < y \t:", (x < y))
   print("x <= y \t:", (x <= y))
   print("x in li \t:", (x in li))
   print("y in li \t:", (y in li))

if __name__ == "__main__":
   main()
