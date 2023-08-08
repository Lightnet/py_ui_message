# https://www.youtube.com/watch?v=RNEcewpVZUQ
# https://stackoverflow.com/questions/14887610/specify-the-dimensions-of-a-tkinter-text-box-in-pixels
# 
# note some off set position and size

import tkinter as tk
import ttkbootstrap as ttk

class App(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    #self.geometry(f"400x200")
    self.geometry('470x550')
    self.resizable(False,False)
    frame_chat = ttk.Frame(self, height=470, width=550, )
    self.frame_chat = frame_chat
    frame_chat.pack(side="top", fill="both", expand=True)
    #head label
    head_label = ttk.Label(frame_chat, text="Welcome")
    head_label.configure(anchor="center")
    head_label.place(relwidth=1)
    #tiny divider
    line = ttk.Label(frame_chat, width=450, background="gray")
    #line.place(relwidth=1, rely=0.07, relheight=0.012)
    
    #scrollbar.configure(command=self.text_widget.yview)
    #text widget
    #self.text_widget = ttk.Text(frame_chat, yscrollcommand=scrollbar.set, width=20, height=2, padx=5, pady=5)
    self.text_widget = ttk.Text(frame_chat, width=20, height=2, padx=5, pady=5)
    self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
    self.text_widget.configure(cursor="arrow", state="disabled")

    scrollbar = ttk.Scrollbar(frame_chat, orient='vertical')
    #scrollbar.place(relheight=0.8,relx=0.974)
    scrollbar.place(relheight=0.734, relx=0.974, rely=0.09)
    #scrollbar.place(relx=0.974, rely=0.09)
    scrollbar.config(command=self.text_widget.yview)
    self.text_widget.configure(yscrollcommand=scrollbar.set)
    #scrollbar.place(height=self.text_widget.winfo_height())


    self.text_widget.configure(state="normal")
    for i in range(100):
      self.text_widget.insert(tk.END, "Welcome to Tutorialspoint...\n\n")
    self.text_widget.configure(state="disabled")

    bottom_label = ttk.Label(frame_chat, background="gray")
    bottom_label.place(relwidth=1,rely=0.825)

    msg_entry = ttk.Entry(frame_chat)
    msg_entry.place(
      relwidth=0.74, 
      relheight=0.09,
      rely=0.89,
      relx=0.011
    )
    msg_entry.focus()
    msg_entry.bind("<Return>",self._on_enter_pressed)
    self.msg_entry = msg_entry

    send_button = ttk.Button(frame_chat, text="Send", width=20,command=lambda: self._on_enter_pressed(None))
    send_button.place(relx=0.77,rely=0.89,relheight=0.09, relwidth=0.22)

  def _on_enter_pressed(self, event):
    msg = self.msg_entry.get()
    self._insert_message( msg, "You")
    self.msg_entry.focus()
    #pass

  def _insert_message(self, msg, sender):
    if not msg:
      return 
    self.msg_entry.delete(0, tk.END)
    msg1 = f"{sender}:{msg}\n"
    self.text_widget.configure(state="normal")
    self.text_widget.insert(tk.END, msg1)
    self.text_widget.configure(state="disabled")

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