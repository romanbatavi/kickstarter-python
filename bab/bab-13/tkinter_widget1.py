######################################################
# Nama file: tkinter_widget1.py
######################################################

# mengimpor modul Tkinter
import tkinter

def main():
   # membuat form utama
   mainform = tkinter.Tk()

   # membuat objek Label
   lbl = tkinter.Label(mainform)
   lbl['text'] = "Masukkan nama Anda"
   lbl.pack()

   # membuat objek Entry
   txt = tkinter.Entry(mainform)
   txt['width'] = 40
   txt.pack()

   # membuat objek Button
   btn = tkinter.Button(mainform)
   btn['text'] = "Klik Saya"
   btn.pack()

   # menampilkan form
   mainform.mainloop()

if __name__ == "__main__":
   main()
