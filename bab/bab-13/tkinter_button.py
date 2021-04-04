######################################################
# Nama file: tkinter_button.py
######################################################

import tkinter
import tkinter.messagebox

def buttonclick():
   tkinter.messagebox.showinfo("Informasi", "Hello Tkinter!")

def main():
   mainform = tkinter.Tk()
   mainform.title("Demo Button")
   mainform.geometry("260x260")
    
   button = tkinter.Button(mainform, background="#335588",
                           foreground="#ffffff", text="Hello",
                           activebackground="#335599",
                           activeforeground="#ff0000",
                           highlightcolor="#ff0000",
                           relief=tkinter.GROOVE,
                           state=tkinter.NORMAL,
                           underline=0,
                           width=10,
                           command=buttonclick)
   button.grid(sticky=tkinter.E+tkinter.S, padx=90, pady=120)
   mainform.mainloop()

if __name__ == "__main__":
   main()
