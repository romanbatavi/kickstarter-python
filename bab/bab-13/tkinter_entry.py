######################################################
# Nama file: tkinter_entry.py
######################################################

import tkinter
import tkinter.messagebox

def main():
   mainform = tkinter.Tk()
   mainform.title("Demo Entry")
   mainform.geometry("250x250")

   # variabel yang akan diasosiasikan
   # dengan kontrol Entry
   var = tkinter.StringVar()
   # menentukan nilai default
   var.set("Python...")

   # fungsi callback
   def kosongkan():
      var.set("")
   def ambilteks():
      tkinter.messagebox.showinfo("Informasi", var.get())
   
   # membuat kontrol Label
   l = tkinter.Label(mainform, text="Masukkan teks")
   l.grid(row=0, column=0, columnspan=2,
          sticky=tkinter.W,
          padx=4, pady=4)

   # membuat kontrol Entry
   e = tkinter.Entry(mainform, textvariable=var)
   e.grid(row=1, column=0, columnspan=2,
          sticky=tkinter.W+tkinter.E,
          padx=4, pady=4)

   # membuat kontrol Button
   b1 = tkinter.Button(mainform, text="Kosongkan",
                       command=kosongkan)
   b1.grid(row=2, column=0, padx=4, pady=4)
   b2 = tkinter.Button(mainform, text="Ambil Teks",
                       command=ambilteks)
   b2.grid(row=2, column=1, padx=4, pady=4)

   mainform.mainloop()

if __name__ == "__main__":
   main()
