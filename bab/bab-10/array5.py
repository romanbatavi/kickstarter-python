######################################################
# Nama file: array5.py
######################################################

import array

# mendefinisikan fungsi untuk mengurutkan elemen array
def sort(A):
   i = 0
   while i < len(A)-1:
      j = len(A)-1
      while j >= i+1:
         if A[j] < A[j-1]:
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
         j -= 1
      i += 1

def main():
   A = array.array('i', [50,10,30,40,20])
   print("Sebelum diurutkan: ")
   for nilai in A:
      print("%d " % nilai, end='')
   print("\n")

   # mengurutkan array
   sort(A)

   print("Setelah diurutkan: ")
   for nilai in A:
      print("%d " % nilai, end='')

if __name__ == "__main__":
   main()
