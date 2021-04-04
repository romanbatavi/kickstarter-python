######################################################
# Nama file: list_remove.py
######################################################

def main():
   list1 = [10, 20, 10, 30, 10]

   print("Sebelum dihapus")
   print("list1: ", list1)

   # menghapus 10 dari list
   list1.remove(10)

   print("\nSetelah dihapus")
   print("list1: ", list1)

if __name__ == "__main__":
   main()
