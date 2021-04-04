######################################################
# Nama file: demodbm.py
######################################################

from os import path
import dbm

class mydbm(object):
   def __init__(self, filename):
      self.db = None      
      if path.exists(filename) and path.isfile(filename):
         self.db = dbm.open(filename, 'w')
      else:
         self.db = dbm.open(filename, 'c')

   def add(self, name, phonenumber):
      if not (name in self.db):
         self.db[name] = phonenumber
         self.db.sync()
      else:
         print("'%s' sudah ada di dalam database" % name)

   def edit(self, name, phonenumber):
      if name in self.db:
         self.db[name] = phonenumber
         self.db.sync()
      else:
         print("'%s' tidak ditemukan dalam database" % name)

   def remove(self, name):
      if name in self.db:
         del self.db[name]
         self.db.sync()
      else:
         print("'%s' tidak ditemukan dalam database" % name)

   def removeall(self):
      self.db.clear()
      self.db.sync()

   def find(self, name):
      if name in self.db:
         return self.db[name]
      else:
         return None

   def listPhonebook(self):
      for k in self.db.keys():
         print("%s\t%s" % (k, self.db[k]))
      print()

   def first(self):
      return self.db.first()

   def previous(self):
      return self.db.previous()

   def next(self):
      return self.db.next()

   def last(self):
      return self.db.last()

   def close(self):
      self.db.close()

def main():
   # membuat objek dari kelas dbm
   db = mydbm("E:\\kodepython\\phonebook1")

   # menambah data
   db.add("ahmad","08152300182")
   db.add("bashori","08562234567")
   db.add("cindy","08122400243")
   db.add("dahlan","08182199555")

   # menampilkan data
   print("SEBELUM DIUBAH:")
   db.listPhonebook()

   # mengubah data
   db.edit("dahlan","08182199777")

   # menghapus data
   db.remove("bashori")

   # menampilkan data setelah diubah dan dihapus
   print("SETELAH DIUBAH:")
   db.listPhonebook()

   # menutup koneksi database
   db.close()

if __name__ == "__main__":
   main()
