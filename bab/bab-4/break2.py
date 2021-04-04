######################################################
# Nama file: break2.py
######################################################

def main():
   for i in range(1,11):
      for j in range(1,11):
         print(i*j, end='\t')
         if j == 5:
            break
      print()

if __name__ == "__main__":
   main()
