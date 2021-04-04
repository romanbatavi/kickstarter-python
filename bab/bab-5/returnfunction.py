######################################################
# Nama file: returnfunction.py
######################################################

# mendefinisikan fungsi pemanggil dengan
# parameter dan nilai kembalian berupa fungsi
def panggil(func):   
   return func

# mendefinisikan fungsi lain
def helloWorld():
   return "Hello World!"

def main():
   # memanggil fungsi panggil() dengan melewatkan
   # fungsi helloWorld() sebagai argumennya
   s = panggil(helloWorld())
   print(s)

if __name__ == "__main__":
   main()
