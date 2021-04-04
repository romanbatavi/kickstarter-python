######################################################
# Nama file: defaultparameter1.py
######################################################

def cetakDaftar(alist=[], urut=False):
   if urut:
      alist.sort()
   for i in alist:
      print(i, end=" ")
   print()
   return

def main():
   # membuat list
   li = [65, 34, 21, 89, 13, 25]

   # memanggil fungsi cetakDaftar()
   print("Data Tidak Terurut")
   cetakDaftar(li)

   print("\nData Terurut")
   cetakDaftar(li, True)

if __name__ == "__main__":
   main()
