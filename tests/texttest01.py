# https://stackoverflow.com/questions/14887610/specify-the-dimensions-of-a-tkinter-text-box-in-pixels
# https://stackoverflow.com/questions/3950687/how-to-find-out-the-current-widget-size-in-tkinter
# https://www.plus2net.com/python/tkinter-geometry.php#:~:text=Resize%20the%20window,values%20are%201%20(%20True%20).
# 

from tkinter import *
root = Tk()
t = Text(root)
t.pack(fill=BOTH, expand=1)
print("height: ",t.winfo_height())

def resize(self):
   print("height: ",t.winfo_height())

root.bind("<Configure>", resize)
root.mainloop()