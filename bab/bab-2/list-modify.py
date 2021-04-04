######################################################
# Nama file: list-modify.py
######################################################

def main():
   # membuat list
   buah = ["durian", "mangga", "apel"]
   print("Sebelum diubah:")
   print(buah)

   # mengubah nilai elemen list
   buah[1] = "salak"
   buah[-1] = "pepaya"

   # menampilkan hasil perubahan
   print("\nSetelah diubah:")
   print(buah)

if __name__ == "__main__":
   main()
