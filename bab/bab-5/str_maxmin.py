######################################################
# Nama file: str_maxmin.py
######################################################

def main():
   str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

   print("str1: ", str1)

   print("\nmax(str1): ", max(str1), \
         " (", ord(max(str1)),")")
   print("min(str1): ", min(str1), \
         " (", ord(min(str1)),")")

if __name__ == "__main__":
   main()
