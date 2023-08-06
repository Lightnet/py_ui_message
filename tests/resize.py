import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1200x800')
root.title("Test")

tab_frame = ttk.Notebook(root)
tab_frame.pack(fill="both", expand=1) # used pack() instead of grid()

s = ttk.Style()
s.configure('test_red.TFrame', background='red')
s.configure('test_green.TFrame', background='green')
s.configure('test_blue.TFrame', background='blue')

tab1 = ttk.Frame(tab_frame, style='test_red.TFrame')
tab2 = ttk.Frame(tab_frame, style='test_blue.TFrame')

tab_frame.add(tab1, text='Tab1')
tab_frame.add(tab2, text='Tab2')

# make two LabelFrames to fill horizontally
tab1.columnconfigure(0, weight=1)
# make two LabelFrames to evenly fill vertically
tab1.rowconfigure((0,1), weight=1)

### frames in tab
label_frame1 = ttk.Labelframe(tab1, text='Label1', style='test_green.TFrame')
label_frame1.grid(sticky="nsew")

label_frame2 = ttk.Labelframe(tab1, text='Label2', style='test_blue.TFrame')
label_frame2.grid(sticky="nsew")

root.mainloop()