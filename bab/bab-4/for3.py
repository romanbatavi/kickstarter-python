######################################################
# Nama file: for3.py
######################################################

def main():
   # membuat list
   daftar = ['Matematika', 'Fisika', 'Kimia']

   # menggunakan for pada tipe list
   for i in range(len(daftar)):
      print("%d: %s" % (i, daftar[i]))

if __name__ == "__main__":
   main()
