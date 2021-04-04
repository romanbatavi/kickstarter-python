######################################################
# Nama file: if-elif2.py
######################################################

def main():
   # input nilai x dan y
   print("Memasukkan data koordinat")
   x = int(input("Masukkan nilai x: "))
   y = int(input("Masukkan nilai y: "))

   info = "Koordinat (" + str(x) + "," + str(y) + \
          ") berada pada Kuadran "

   # memeriksa nilai x dan y
   if x > 0 and y > 0:
      print(info + "I")
   elif x < 0 and y > 0:
      print(info + "II")
   elif x < 0 and y < 0:
      print(info + "III")
   elif x > 0 and y < 0:
      print(info + "IV")
   else:
      pass

if __name__ == "__main__":
   main()
