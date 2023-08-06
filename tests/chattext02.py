import tkinter as tk


class ChatView(tk.Frame):
  def __init__(self, *args, **kwargs):
    tk.Frame.__init__(self, *args, **kwargs)
    left_frame = tk.Frame(self,background="gray")
    middle_frame = tk.Frame(self)
    right_frame = tk.Frame(self, background="red")

    #left_frame.pack(side="left",expand=False)
    #middle_frame.pack(expand=True)
    #right_frame.pack(side="right",expand=False)

    left_frame.grid(row=0,column=0,sticky='nesw')
    middle_frame.grid(row=0,column=1,sticky='nesw')
    right_frame.grid(row=0,column=2,sticky='nesw')
    

    button_left = tk.Button(left_frame,text="Hello")
    button_left.pack()

    text_middle = tk.Text(middle_frame)
    text_middle.grid(row=0,column=0)

    text_bottom = tk.Text(middle_frame,height=2)
    text_bottom.grid(row=1,column=0)

    #text_middle.insert(tk.INSERT, "Hello.....")
    #text_middle.pack()
    #button_right = tk.Button(middle_frame,text="middle")
    #button_right.grid(row=0,column=0)
    

    button_right = tk.Button(right_frame,text="Hello")
    button_right.grid(row=0,column=0)
    #button_right.pack()

    imput = tk.Entry(right_frame, width=50)
    imput.grid(row=0,column=1,sticky='we')



if __name__ == "__main__":
    root = tk.Tk()
    view = ChatView(root)
    view.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x200")
    root.mainloop()