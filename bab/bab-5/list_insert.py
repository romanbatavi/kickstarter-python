######################################################
# Nama file: list_insert.py
######################################################

def main():
   list1 = [10, 20, 30]

   print("Sebelum ditambah")
   print("list1: ", list1)

   # menambah elemen baru pada posisi kedua
   list1.insert(1, 90)

   print("\nSetelah ditambah")
   print("list1: ", list1)

if __name__ == "__main__":
   main()
