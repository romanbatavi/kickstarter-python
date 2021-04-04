######################################################
# Nama file: str_replace.py
######################################################

def main():
   str1 = "I like Python! I like C++! I like C!"

   print("str1: ", str1)
   str2 = str1.replace("like", "love")
   str3 = str1.replace("like", "love", 2)

   print("str2: ", str2)
   print("str3: ", str3)

if __name__ == "__main__":
   main()
