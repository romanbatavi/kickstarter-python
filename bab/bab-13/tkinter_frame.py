######################################################
# Nama file: tkinter_frame.py
######################################################

# mengimpor modul Tkinter
import tkinter

def main():
   mainform = tkinter.Frame()
   mainform.grid()

   btnKeluar = tkinter.Button(mainform, 
                  text="Keluar", command=quit)
   btnKeluar.grid(sticky=tkinter.E+tkinter.S, padx=90, pady=90)

   mainform.master.title("Demo Frame")
   mainform.mainloop()

if __name__ == "__main__":
   main()
