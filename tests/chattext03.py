# https://ttkbootstrap.readthedocs.io/en/latest/gettingstarted/tutorial/
# https://www.digitalocean.com/community/tutorials/tkinter-working-with-classes
import tkinter as tk
import ttkbootstrap as ttk


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Go to the Side Page",
            command=lambda: controller.show_frame(SidePage),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class SidePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is the Side Page")
        label.pack(padx=10, pady=10)

        switch_window_button = tk.Button(
            self,
            text="Go to the Completion Screen",
            command=lambda: controller.show_frame(CompletionScreen),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)


class CompletionScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Completion Screen, we did it!")
        label.pack(padx=10, pady=10)
        switch_window_button = ttk.Button(
            self, text="Return to menu", command=lambda: controller.show_frame(MainPage)
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

class App(tk.Tk):
  def __init__(self, *args, **kwargs):
    tk.Tk.__init__(self, *args, **kwargs)
    #self.geometry('400x200')
    #frame_chat = ttk.Frame(self, height=400, width=600, )
    #frame_chat.pack(side="top", fill="both", expand=True)
    #frame_chat.

    #button_test = ttk.Button(frame_chat,text="Hello")
    #button_test.pack()

    # creating a frame and assigning it to container
    container = tk.Frame(self, height=400, width=600)
    # specifying the region where the frame is packed in root
    container.pack(side="top", fill="both", expand=True)

    # configuring the location of the container using grid
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # We will now create a dictionary of frames
    self.frames = {}
    # we'll create the frames themselves later but let's add the components to the dictionary.
    for F in (MainPage, SidePage, CompletionScreen):
        frame = F(container, self)

        # the windows class acts as the root window for the frames.
        self.frames[F] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    # Using a method to switch frames
    self.show_frame(MainPage)
    #pass

  def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()
    



if __name__ == "__main__":
  #root = tk.Tk()
  #view = ChatView(root)
  #view.pack(side="top", fill="both", expand=True)
  #root.wm_geometry("400x200")
  #root.mainloop()
  app = App()
  app.mainloop()
  pass