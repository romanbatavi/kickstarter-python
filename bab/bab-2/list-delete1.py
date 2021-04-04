######################################################
# Nama file: list-delete1.py
######################################################

def main():
   # membuat list
   buah = ["durian", "mangga", "apel", "apel", "durian", "apel"]
   print("Sebelum dihapus:")
   print(buah)

   # menghapus elemen list
   buah.remove("durian")
   buah.remove("apel")

   # menampilkan hasil setelah dihapus
   print("\nSetelah dihapus:")
   print(buah)

if __name__ == "__main__":
   main()
