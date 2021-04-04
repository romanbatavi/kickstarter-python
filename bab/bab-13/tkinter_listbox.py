######################################################
# Nama file: tkinter_listbox.py
######################################################

import tkinter
import tkinter.messagebox

def main():
   mainform = tkinter.Tk()
   mainform.title("Demo Listbox")
   mainform.geometry("250x250")

   def getchoice():
      tkinter.messagebox.showinfo("Informasi",
                            lb.get(lb.curselection()))

   # membuat kontrol Label
   l = tkinter.Label(mainform, text="Bahasa pemrograman:")
   l.grid(row=0, sticky=tkinter.W, padx=4, pady=4)

   # membuat kontrol Listbox
   lb = tkinter.Listbox(mainform)
   lb.insert(0, "Python")
   lb.insert(1, "Perl")
   lb.insert(2, "Ruby")
   lb.insert(3, "PHP")
   lb.grid(row=1, sticky=tkinter.W, padx=4, pady=4)

   # membuat kontrol Button
   b = tkinter.Button(mainform, text="Info Pilihan",
                      command=getchoice)
   b.grid(row=2, sticky=tkinter.W, padx=4, pady=4)
   mainform.mainloop()

if __name__ == "__main__":
   main()
