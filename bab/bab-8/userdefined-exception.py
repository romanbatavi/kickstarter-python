######################################################
# Nama file: userdefined-exception.py
######################################################

import math

# membuat eksepsi AbstractError
class AbstractError(RuntimeError):
   def __init__(self, s):
      self.s = s

# mendefinisikan kelas abstrak
class DuaDimensi(object):
   def __init__(self):
      raise AbstractError("ERROR: '" + 
            "DuaDimensi" + 
            "' adalah kelas abstrak")
   def luas(self):
      raise NotImplementedError
   def keliling(self):
      raise NotImplementedError

# membuat kelas Lingkaran,
# turunan dari kelas DuaDimensi
class Lingkaran(DuaDimensi):
   def __init__(self, r):
      self.r = r
   def luas(self):
      return math.pi * self.r * self.r
   def keliling(self):
      return 2 * math.pi * self.r

def main():
   # instansiasi kelas Lingkaran : BENAR
   obj1 = Lingkaran(3)

   print("LINGKARAN")
   print("Luas\t:", obj1.luas())
   print("Keliling\t:", obj1.keliling())

   # instansiasi kelas DuaDimensi : SALAH
   try:
      print("\nMembuat objek " + 
            "dari kelas DuaDimensi...")
      obj2 = DuaDimensi()
   except AbstractError as error:
      print(error.s)
   else:
      print("DUADIMENSI")
      print("Luas\t:", obj2.luas())
      print("Keliling\t:", obj2.keliling())

if __name__ == "__main__":
   main()
