######################################################
# Nama file: write.py
######################################################

def main():
   # membuka file
   f = open("data.txt", "w")

   # menulis data ke dalam file
   f.write("Mudah Belajar Python\n")
   f.write("2019\n")

   # menutup file
   f.close()

if __name__ == "__main__":
   main()
