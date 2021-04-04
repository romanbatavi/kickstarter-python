######################################################
# Nama file: tkinter_callback.py
######################################################

# mengimpor modul Tkinter
import tkinter
import tkinter.messagebox

def main():
   mainform = tkinter.Tk()

   # mendefinisikan fungsi
   def buttonclick():
      tkinter.messagebox.showinfo("Hallo", 
         "Hallo %s, apa kabar?" % (txt.get()))

   lbl = tkinter.Label(mainform)
   lbl['text'] = "Masukkan nama Anda"
   lbl.pack()

   txt = tkinter.Entry(mainform)
   txt['width'] = 40
   txt.pack()

   btn = tkinter.Button(mainform,
                        command=buttonclick)
   btn['text'] = "Klik Saya"
   btn.pack()

   # menampilkan form
   mainform.mainloop()

if __name__ == "__main__":
   main()
