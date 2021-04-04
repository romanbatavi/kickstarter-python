######################################################
# Nama file: mainform1.py
######################################################

# mengimpor modul Tkinter
import tkinter

def main():
   # membuat form utama
   mainform = tkinter.Tk()

   # mengubah title bar
   mainform.wm_title("Hello Tkinter")

   # mengubah warna form
   mainform['background'] = "#bbc9c9"

   #################################################
   # di sini tempat Anda menempatkan kontrol-kontrol
   # lain di dalam form
   #################################################

   # menampilkan form
   mainform.mainloop()

if __name__ == "__main__":
   main()
