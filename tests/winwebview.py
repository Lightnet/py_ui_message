#install pywebview

# Import tkinter and webview libraries
from tkinter import *
#import webbrowser
import webview

#webview.create_window('Hello world', 'https://www.youtube.com/')
#webview.start()


# creating root
root = Tk()

# setting GUI title
root.title("WebBrowsers")
  
# setting GUI geometry
root.geometry("660x660")
  
# call webbrowser.open() function.
#webbrowser.open("www.instagram.com")

def load_html(window):
  window.load_html('<html><body><h1>pywebview wow!</h1><body></html>')

window = webview.create_window('pywebview wow')
webview.start(load_html, window)