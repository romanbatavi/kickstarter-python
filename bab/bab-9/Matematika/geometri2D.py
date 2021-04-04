# Nama file: geometri2D.py

import math

# fungsi luas persegi panjang
def luasPersegiPanjang(p, l):
   return p * l

# fungsi keliling persegi panjang
def kelilingPersegiPanjang(p, l):
  return 2 * (p+l)

# fungsi luas bujursangkar
def luasBujursangkar(s):
  return s * s

# fungsi keliling bujursangkar
def kelilingBujursangkar(s):
  return 4 * s

# fungsi luas lingkaran
def luasLingkaran(r):
   return math.pi * r * r

# fungsi keliling lingkaran
def kelilingLingkaran(r):
   return 2 * math.pi * r

# fungsi luas segitiga
def luasSegitiga(a, t):
   return (a * t) / 2

# fungsi keliling segitiga
def kelilingSegitiga(a, b, c):
   return a + b + c
