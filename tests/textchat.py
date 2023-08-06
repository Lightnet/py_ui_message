# https://stackoverflow.com/questions/46081798/automatically-resize-text-widgets-height-to-fit-all-text
# https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/
# https://stackoverflow.com/questions/16523128/resizing-tkinter-frames-with-fixed-aspect-ratio
import tkinter as tk
from tkinter import INSERT, Toplevel, ttk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo
import os

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ExpandoText(tk.Text):
  def insert(self, *args, **kwargs):
    result = ttk.Text.insert(self, *args, **kwargs)
    self.reset_height()
    return result

  def reset_height(self):
    height = self.tk.call((self._w, "count", "-update", "-displaylines", "1.0", "end"))
    self.configure(height=height)

class App(ThemedTk):
  def __init__(self):
    super().__init__()
    self.title("Test")
    self.geometry("600x400")
    self.resizable(True,True)
    #self.columnconfigure(0, weight=1)
    #self.rowconfigure(0, weight=1)
    frame_chat = tk.Frame(self)
    frame_chat.pack(fill="both",expand=1)

    lable1 = tk.Label(frame_chat, text="Welcome").grid(row=0)
 
    txt = tk.Text(frame_chat, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
    txt.grid(row=1, column=0, columnspan=2)
    
    scrollbar = tk.Scrollbar(txt)
    scrollbar.place(relheight=1, relx=0.001)
    #scrollbar.place(relheight=1, relx=0.974)
    
    #e = tk.Entry(frame_chat, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
    #e.grid(row=2, column=0)
    
    #button_send = tk.Button(frame_chat, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                  #command=self.send).grid(row=2, column=1)

  def resize_frame(self, e):
    pass

  def send(self):
    print("SEND MESSAGE")
    pass

if __name__ == "__main__":
  app = App()
  app.mainloop()