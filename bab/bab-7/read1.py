######################################################
# Nama file: read1.py
######################################################

def main():
   # membuka file
   f = open("data.txt", "r")

   # membaca data 13 byte di dalam file
   s = f.read(13)

   print("DATA: ")
   print(s)
   
   # menutup file
   f.close()

if __name__ == "__main__":
   main()
