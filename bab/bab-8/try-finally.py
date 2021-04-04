######################################################
# Nama file: try-finally.py
######################################################

def main():
   try:
      # membuka file
      f = open("data.txt", "w")

      try:
         # menulis data ke file
         f.write("Pemrograman Python")
      finally:
         f.close()  # menutup file
   except IOError:
      print("\nERROR: File tidak dapat " +
            "dibuka/ditulis")

if __name__ == "__main__":
   main()
