######################################################
# Nama file: wordcounter.py
######################################################

from collections import Counter

def wordCounter(word, source):
   li = source.split(' ')
   words = Counter(li).most_common()
   d = {}
   for w in words:
      d[w[0]] = w[1]
   try:
      print("%s : %d" % (word, d[word]))
   except KeyError as e:
      print("%s : 0" % word)

def main():
   source = "Python Perl PHP Python Ruby Python PHP"

   word = input("Masukkan kata yang dicari: ")

   # mencari jumlah kata
   wordCounter(word, source)

if __name__ == "__main__":
   main()
