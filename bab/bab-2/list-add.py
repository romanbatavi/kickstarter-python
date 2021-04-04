######################################################
# Nama file: list-add.py
######################################################

def main():
   # membuat list
   buah = ["durian", "mangga", "apel"]
   print("Elemen awal:")
   print(buah)

   # menggunakan metode append()   
   buah.append("jeruk")
   print("\nSetelah append():")
   print(buah)

   # menggunakan metode insert()
   buah.insert(1, "kiwi")
   print("\nSetelah insert():")
   print(buah)

   # menggunakan metode extend()
   buah.extend(["melon", "anggur"])
   print("\nSetelah append():")
   print(buah)

if __name__ == "__main__":
   main()
