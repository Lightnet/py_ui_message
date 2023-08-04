# https://www.pythontutorial.net/tkinter/tkinter-object-oriented-window/
# https://www.pythontutorial.net/tkinter/ttk-style/
# https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-theme-layer.html
# https://python-course.eu/tkinter/entry-widgets-in-tkinter.php
# https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# https://www.geeksforgeeks.org/python-menu-widget-in-tkinter/
# 



# entry point
import tkinter as tk
from tkinter import Toplevel, ttk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo
import os

#class App(tk.Tk):
class App(ThemedTk):

  def __init__(self):
    super().__init__()
    self.filepath = "raw_data.csv"

    # Adding a title to the window
    self.wm_title("Message")
    self.geometry("400x300")
    #self.tk.call('source', 'azure/azure.tcl')

    # Create a style
    style = ttk.Style(self)
    #print("style:", style)
    #style.theme_use('azure')
    #style.theme_use('aquativo')
    #print("themes:", style.theme_names())
    style.theme_use('yaru')

    self.ui_menu_bar()
    self.ui_login()
    #print("self: ", self)

  def ui_menu_bar(self):
    #win = Toplevel(self)
    # Creating Menubar
    menubar = tk.Menu(self)
    # Adding File Menu and commands
    file_menu = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file_menu)
    file_menu.add_command(label="New", command=self.donothing)
    file_menu.add_command(label="Open", command=self.donothing)
    file_menu.add_command(label="Settings", command=self.donothing)
    file_menu.add_command(label='Exit',command=self.destroy)

    file_menu.entryconfig(0, state=tk.DISABLED)
    file_menu.entryconfig(1, state=tk.DISABLED)
    #file_menu.entryconfig(3, state=tk.DISABLED)

    # Adding Groups Menu
    groups_ = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Groups', menu = groups_)
    groups_.add_command(label ='Create', command = None)
    groups_.add_command(label ='Join', command = None)
    groups_.add_command(label ='Find', command = None)
    groups_.add_command(label ='Invite', command = None)
    menubar.entryconfig(2, state=tk.DISABLED)

    # Adding Contacts Menu
    contacts_ = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Contacts', menu = contacts_)
    contacts_.add_command(label ='Invite', command = None)
    contacts_.add_command(label ='Pending', command = None)
    contacts_.add_command(label ='Delete', command = None)
    contacts_.add_command(label ='Blacklist', command = None)
    menubar.entryconfig(3, state=tk.DISABLED)

    party_ = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Party', menu = party_)
    party_.add_command(label ='Create', command = None)
    party_.add_command(label ='Join', command = None)
    party_.add_command(label ='Delete', command = None)
    party_.add_command(label ='Kick', command = None)
    party_.add_command(label ='Admin', command = None)
    self.menu_party = party_
    menubar.entryconfig(4, state=tk.DISABLED)

    # Adding Help Menu
    help_ = tk.Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='Demo', command = None)
    help_.add_separator()
    help_.add_command(label ='About Tk', command = None)

    # display Menu
    #self.config(menu = file_menu)
    self.config(menu = menubar)


  def event_win_quit(self):
    print("QUIT")
    self.destroy()
    os._exit(os.EX_OK)
    #pass

  def ui_login(self):
    self.frame_login = tk.Frame()
    self.frame_login.pack()
    # LABEL & INPUT
    label_section = ttk.Label(self.frame_login, text="LOGIN ACCESS!")

    label_name = ttk.Label(self.frame_login, text="Alias:")
    self.input_name = ttk.Entry(self.frame_login)
    label_passphrase = ttk.Label(self.frame_login,text="Passphrase:")
    input_passphrase = ttk.Entry(self.frame_login)
    # 
    #label_email = ttk.Label(self.frame_login,text="E-Mail")
    #label_email.grid(row = 2, column = 0)
    #self.input_email = ttk.Entry(self.frame_login)
    #self.input_email.grid(row = 2, column = 1)
    # button
    btn_quit = ttk.Button(self.frame_login, text='Quit')
    btn_quit['command'] = self.event_win_quit
    bottom_frame = tk.Frame(self.frame_login)
    btn_login = ttk.Button(bottom_frame, text='Login')
    btn_login['command'] = self.event_signin
    btn_signup = ttk.Button(bottom_frame, text='Sign Up')
    btn_signup['command'] = self.change_signup
    # GRID
    label_section.grid(row = 0, column = 0,columnspan=3,pady=20)
    label_name.grid(row = 1, column = 0)
    self.input_name.grid( row = 1, column = 1, columnspan=2)
    label_passphrase.grid(row = 2, column = 0)
    input_passphrase.grid(row = 2, column = 1, columnspan=2)

    btn_quit.grid(row = 3, column=0,pady=10)

    bottom_frame.grid(row=3,column=1, columnspan=2,pady=10)
    btn_login.grid(row = 0, column=0)
    btn_signup.grid(row = 0, column=1)

  def ui_recovery(self):
    pass

  def ui_forgot(self):
    pass

  def change_signup(self):
    #remove frame
    self.frame_login.pack_forget()
    self.ui_signup()

  def event_signin(self):
    #check account pass else error
    self.frame_login.pack_forget()
    self.ui_home()
    #pass

  def ui_home(self):
    self.frame_login.pack_forget()

    #self.option_add('*tearOff', False)

    #win = Toplevel(self)
    """
    menubar = tk.Menu(self, tearoff=False)
    print("self: ", self)
    #win['menu'] = menubar
    self.config(menu=menubar)
    #filemenu = Menu(menubar, tearoff=0)
    file_menu = menubar
    file_menu.add_command(
      label='Exit',
      command=self.destroy
    )"""
    """
    filemenu.add_command(label="New", command=self.donothing)
    filemenu.add_command(label="New", command=self.donothing)
    filemenu.add_command(label="Open", command=self.donothing)
    filemenu.add_command(label="Save", command=self.donothing)
    filemenu.add_command(label="Save as...", command=self.donothing)
    filemenu.add_command(label="Close", command=self.donothing)
    """

    self.frame_home = tk.Frame()
    self.frame_home.pack()

    self.label_frame = ttk.Label(self.frame_home, text="Home")
    self.label_frame.grid(row = 0, column = 0)

    self.label_contact = ttk.Label(self.frame_home, text="Contacts")
    self.label_contact.grid(row = 1, column = 0)

    self.label_contact = ttk.Label(self.frame_home, text="Groups")
    self.label_contact.grid(row = 2, column = 0)

  def donothing(self):
   filewin = Toplevel(self)
   button = ttk.Button(filewin, text="Do nothing button")
   #button = ttk.Button(self, text="Do nothing button")
   button.pack()

  def ui_signup(self):
    
    #add new frame
    self.frame_signup = tk.Frame()
    self.frame_signup.pack()
    
    # label & INPUT
    label_name = ttk.Label(self.frame_signup, text="Alias")
    self.input_name = ttk.Entry(self.frame_signup)
    label_passphrase = ttk.Label(self.frame_signup,text="Passphrase")
    input_passphrase = ttk.Entry(self.frame_signup)
    label_email = ttk.Label(self.frame_signup,text="E-Mail")
    self.input_email = ttk.Entry(self.frame_signup)
    bottom_frame = tk.Frame(self.frame_signup)
    bottom_frame.grid(row=3,column=0, columnspan=2)

    # button
    btn_login = ttk.Button(bottom_frame, text='Register')
    btn_login['command'] = self.event_register
    btn_signup = ttk.Button(bottom_frame, text='Cancel')
    btn_signup['command'] = self.back_signup_to_login
    
    # LAYOUT GRID
    label_name.grid(row = 0, column = 0)
    self.input_name.grid( row = 0, column = 1)
    label_passphrase.grid(row = 1, column = 0)
    input_passphrase.grid(row = 1, column = 1)
    label_email.grid(row = 2, column = 0)
    self.input_email.grid(row = 2, column = 1)
    btn_login.grid(row = 0, column = 0)
    btn_signup.grid(row = 0, column = 1)

  def back_signup_to_login(self):
    self.frame_signup.pack_forget()
    self.ui_login()

  def event_register(self):
    print("inputPassphrase: ",self.inputPassphrase.get())

    input_name = self.inputName.get()
    input_passphrase = self.inputPassphrase.get()
    input_email = self.inputEmail.get()
    
    #showinfo(title='Information', message='Hello, Tkinter!')
    """if not os.path.exists(self.filepath):
      mydataset = {
        'name': [],
        'passphrase': [],
        'email': []
      }
      df = pd.DataFrame(mydataset)
      print(df)
      df.to_csv(self.filepath, index=False)
    else:
      df = pd.read_csv(self.filepath)
      # Insert Dict to the dataframe using DataFrame.append()
      new_row = {'name':input_name, 'passphrase':input_passphrase, 'email':input_email}
      df = df._append(new_row, ignore_index=True)
      df.to_csv('raw_data.csv', index=False)"""
  # add contact
  def ui_add_contact(self):
    pass
  # create group
  def ui_create_group(self):
    pass
  #list group join
  def ui_view_groups(self):
    pass
  # admin area
  def ui_admin_group(self):
    pass
  # kick or ban user
  def ui_kick_member(self):
    pass
  # edit user permission
  def ui_member_permission(self):
    pass
  #user room
  def ui_chat_room(self):
    pass

#def run():
  #print("Py tkinter!")
  #app = appWindowUI()
  #app.mainloop()