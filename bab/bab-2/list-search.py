######################################################
# Nama file: list-search.py
######################################################

def main():
   # membuat list
   buah = ["durian", "mangga", "apel"]
   print(buah)

   # mencari elemen list
   print('"durian" berada pada indeks ke-%d' %
         buah.index("durian"))
   print('"apel" berada pada indeks ke-%d' %
         buah.index("apel"))

if __name__ == "__main__":
   main()
