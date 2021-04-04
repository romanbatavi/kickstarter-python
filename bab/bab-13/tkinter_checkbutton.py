######################################################
# Nama file: tkinter_checkbutton.py
######################################################

import tkinter
import tkinter.messagebox

def main():
   mainform = tkinter.Tk()
   mainform.title("Demo Checkbutton")
   mainform.geometry("250x250")
   
   # variabel yang akan dihubungkan
   # ke kontrol-kontrol Checkbutton
   var1 = tkinter.IntVar()
   var2 = tkinter.IntVar()
   var3 = tkinter.IntVar()

   # fungsi lokal
   def getchoice():
      pilihan = [];
      if var1.get() == 1: pilihan.append("Mendengarkan musik")
      if var2.get() == 1: pilihan.append("Menonton film")
      if var3.get() == 1: pilihan.append("Berolahraga")         
      tkinter.messagebox.showinfo("Informasi",
                            str(pilihan))

   # membuat kontrol Label
   l = tkinter.Label(mainform, text="Hobi Anda:")
   l.grid(row=0, sticky=tkinter.W)

   # membuat kontrol-kontrol Checkbutton
   c1 = tkinter.Checkbutton(mainform, variable=var1,
                            text="Mendengarkan musik")
   c1.grid(row=1, sticky=tkinter.W)
   c2 = tkinter.Checkbutton(mainform, variable=var2,
                            text="Menonton film")
   c2.grid(row=2, sticky=tkinter.W)
   c3 = tkinter.Checkbutton(mainform, variable=var3,
                            text="Berolahraga")
   c3.grid(row=3, sticky=tkinter.W)

   # membuat kontrol Button
   b1 = tkinter.Button(mainform, text="OK", command=getchoice,
                       width=10)
   b1.grid(row=4, sticky=tkinter.W, padx=4, pady=4)
   b2 = tkinter.Button(mainform, text="Keluar", command=quit,
                       width=10)
   b2.grid(row=4, sticky=tkinter.W, padx=90, pady=4)

   mainform.mainloop()

if __name__ == "__main__":
   main()
