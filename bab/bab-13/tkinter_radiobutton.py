######################################################
# Nama file: tkinter_radiobutton.py
######################################################

import tkinter

def main():
   mainform = tkinter.Tk()
   mainform.title("Demo Radiobutton")
   mainform.geometry("250x250")

   # membuat variabel yang beraosiasi dengan kontrol
   var = tkinter.IntVar()

   def radiobuttonselect():
      pilihan = "Anda memilih: " + str(var.get())
      label.config(text=pilihan)
   
   # membuat kontrol Radiobutton
   rb1 = tkinter.Radiobutton(mainform, text="Perl",
                             variable=var, value=0,
                             command=radiobuttonselect)
   rb1.grid(row=0, sticky=tkinter.W)
   rb2 = tkinter.Radiobutton(mainform, text="Python",
                             variable=var, value=1,
                             command=radiobuttonselect)
   rb2.grid(row=1, sticky=tkinter.W)
   rb3 = tkinter.Radiobutton(mainform, text="Ruby",
                             variable=var, value=2,
                             command=radiobuttonselect)
   rb3.grid(row=2, sticky=tkinter.W)

   # membuat kontrol Label (untuk menampilkan hasil)
   label = tkinter.Label(mainform)
   label.grid(row=3, sticky=tkinter.W, pady=6)

   mainform.mainloop()

if __name__ == "__main__":
   main()
