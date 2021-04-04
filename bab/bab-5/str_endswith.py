######################################################
# Nama file: str_endswith.py
######################################################

def main():
   str = "hello world!"

   print(str.endswith("world"))
   print(str.endswith("world!"))
   print(str.endswith("lo", 3, 5))

if __name__ == "__main__":
   main()
