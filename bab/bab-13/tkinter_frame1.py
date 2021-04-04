######################################################
# Nama file: tkinter_frame1.py
######################################################

# mengimpor modul Tkinter
import tkinter

# membuat kelas DemoFrame 
# yang diturunkan dari kelas Frame
class DemoFrame(tkinter.Frame):
  # konstruktor DemoFrame
  def __init__(self, master=None):
    # memanggil konstruktor kelas induk (tkinter.Frame)
    tkinter.Frame.__init__(self, master)
    self.grid()
    self.buatKontrol()

  # membuat dan menempatkan kontrol ke dalam frame
  def buatKontrol(self):
    self.btnKeluar = tkinter.Button(self, 
                        text="Keluar", command=self.quit)
    self.btnKeluar.grid(sticky=tkinter.E, padx=90, pady=90)

def main():
   # membuat kelas DemoFrame
   app = DemoFrame()
   app.master.title("Demo Frame")
   app.mainloop()

if __name__ == "__main__":
   main()
