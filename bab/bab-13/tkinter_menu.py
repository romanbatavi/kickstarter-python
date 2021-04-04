######################################################
# Nama file: tkinter_menu.py
######################################################

import tkinter
import tkinter.messagebox

def main():
   mainform = tkinter.Tk()
   mainform.title("Demo Menu")
   mainform.geometry("250x100")

   def item1click():
      tkinter.messagebox.showinfo("Informasi","Item 1 di-klik")

   def item2click():
      tkinter.messagebox.showinfo("Informasi","Item 2 di-klik")

   def notimplemented():
      tkinter.messagebox.showinfo("Informasi","Belum diimpelementasi")

   # membuat menubar
   menubar = tkinter.Menu(mainform)
   
   # membuat menu Aplikasi
   appmenu = tkinter.Menu(menubar, tearoff=0)
   appmenu.add_command(label="Item 1", command=item1click)
   appmenu.add_command(label="Item 2", command=item2click)
   appmenu.add_separator()
   appmenu.add_command(label="Keluar", command=quit)

   menubar.add_cascade(label="Aplikasi", menu=appmenu)

   # membuat menu Bantuan
   helpmenu = tkinter.Menu(menubar, tearoff=0)
   helpmenu.add_command(label="Cara menggunakan program",
                        command=notimplemented)
   helpmenu.add_separator()
   helpmenu.add_command(label="Tentang program",
                        command=notimplemented)

   menubar.add_cascade(label="Bantuan", menu=helpmenu)

   mainform.config(menu=menubar)
   mainform.mainloop()

if __name__ == "__main__":
   main()
