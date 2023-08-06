# https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/
# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
import tkinter as tk
import ttkbootstrap as ttk

class App(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    self.geometry(f"400x200")
    #self.geometry('400x200')
    frame_chat = ttk.Frame(self, height=400, width=600, )
    frame_chat.pack(side="top", fill="both", expand=True)
    #frame_chat.

    button_test = ttk.Button(frame_chat,text="Hello")
    button_test['command'] = self.resize
    button_test.pack()

  def resize(self):
    w = 500
    h = 500
    self.geometry(f"{w}x{h}")

if __name__ == "__main__":
  #root = tk.Tk()
  #view = ChatView(root)
  #view.pack(side="top", fill="both", expand=True)
  #root.wm_geometry("400x200")
  #root.mainloop()
  app = App()
  app.mainloop()
  pass