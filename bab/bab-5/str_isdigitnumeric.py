######################################################
# Nama file: str_isdigitnumeric.py
######################################################

def main():
   str1 = "thesecret2006"
   str2 = '0123456789'

   print("str1: " + str1)
   print("str2: " + str2)
   print("\nstr1.isdigit(): ", 
          str1.isdigit())
   print("str1.isnumeric(): ", 
          str1.isnumeric())
   print("\nstr2.isdigit(): ", 
          str2.isdigit())
   print("str2.isnumeric(): ", 
          str2.isnumeric())

if __name__ == "__main__":
   main()
