######################################################
# Nama file: list_pop.py
######################################################

def main():
   list1 = [10, 20, 30, 40, 50]

   print("Sebelum diambil")
   print("list1: ", list1)

   # mengambil 50 dari list
   list1.pop()

   # mengambil 40 dari list
   list1.pop()

   print("\nSetelah diambil")
   print("list1: ", list1)

if __name__ == "__main__":
   main()
