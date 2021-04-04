######################################################
# Nama file: str_isalnumspace.py
######################################################

def main():
   str1 = "thesecret2006"  # tidak ada spasi
   str2 = ' ' # karakter spasi
   str3 = "ThepowerThemagic"

   print("str1: " + str1)
   print("str2: " + str2)
   print("str3: " + str3)

   print("\nstr1.isalnum(): ",
          str1.isalnum())
   print("str1.isalpha(): ", 
          str1.isalpha())
   print("str1.isspace(): ", 
          str1.isspace())

   print("\nstr2.isalnum(): ", 
          str2.isalnum())
   print("str2.isalpha(): ", 
          str2.isalpha())
   print("str2.isspace(): ", 
          str2.isspace())

   print("\nstr3.isalnum(): ", 
          str3.isalnum())
   print("str3.isalpha(): ", 
          str3.isalpha())
   print("str3.isspace(): ", 
          str3.isspace())

if __name__ == "__main__":
   main()
