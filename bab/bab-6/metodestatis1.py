######################################################
# Nama file: metodestatis1.py
######################################################

import math

class hitung(object):
   def __init__(self, p, l, t):
      pass

   @staticmethod
   def log10(x):
      return math.log10(x)

   @staticmethod
   def log(x):
      return math.log(x)

   @staticmethod
   def kali(x, y):
      return x * y

   @staticmethod
   def pangkat(x, y):
      return math.pow(x, y)

   @staticmethod
   def akar(x):
      return math.sqrt(x)

   @staticmethod
   def absolut(x):
      return abs(x)

def main():
   print("hitung.log10(1000) \t= %f" % hitung.log10(1000))
   print("hitung.log(4) \t\t= %f" % hitung.log(4))
   print("hitung.kali(2, 4) \t= %f" % hitung.kali(2, 4))
   print("hitung.pangkat(3, 4) \t= %f" % hitung.pangkat(3, 4))
   print("hitung.akar(81) \t= %f" % hitung.akar(81))
   print("hitung.absolut(-8) \t= %f" % hitung.absolut(-8))

if __name__ == "__main__":
   main()
