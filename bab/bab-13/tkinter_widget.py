######################################################
# Nama file: tkinter_widget.py
######################################################

# mengimpor modul Tkinter
import tkinter

def main():
   # membuat form utama
   mainform = tkinter.Tk()

   # membuat objek Button
   btn = tkinter.Button(mainform)

   # mengubah warna form
   btn['text'] = "Klik Saya"
   btn['background'] = "#66ccff"

   # menempatkan kontrol ke dalam form
   # menggunakan Pack Manager
   btn.pack(padx=30, pady= 20)

   # menampilkan form
   mainform.mainloop()

if __name__ == "__main__":
   main()
