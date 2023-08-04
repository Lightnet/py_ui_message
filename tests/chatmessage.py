# https://realpython.com/python-gui-tkinter/
# 

import tkinter as tk
from tkinter import Toplevel, ttk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo
import os

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

#class App(tk.Tk):
class App(ThemedTk):
  def __init__(self):
    super().__init__()
    # Adding a title to the window
    self.wm_title("Message")
    self.geometry("840x640")

    # set up a style
    style = ttk.Style(self)
    style.theme_use('yaru')

    self.frame_chat = tk.Frame()

    #lable1 = tk.Label(self.frame_chat, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)
 
    txt = tk.Text(self.frame_chat, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
    txt.grid(row=1, column=0, columnspan=2)
    
    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.974)
    
    e = tk.Entry(self.frame_chat, 
      bg="#2C3E50", 
      fg=TEXT_COLOR, 
      font=FONT, 
      width=55
    )
    e.grid(row=2, column=0)
    
    send = tk.Button(self.frame_chat, 
      text="Send", 
      font=FONT_BOLD, 
      bg=BG_GRAY,
      command=None
    ).grid(row=2, column=1)
    
    self.frame_chat.pack()

if __name__ == "__main__":
  app = App()
  app.mainloop()