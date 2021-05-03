import webbrowser
import easyocr
from PIL import ImageGrab
from tkinter import *
from tkinter import messagebox
import pyperclip
def clr():
    global out
    out.delete('1.0', END)
def textg():
    clr()
    try:
        global reader
        global out
        img = ImageGrab.grabclipboard()
        img.save('snip.png', 'PNG')
        file_name = "snip.png"
        output = reader.readtext(file_name)
        b = ''
        for a in output:
            b += a[1]
            b += ' '
        g(b)
    except:
        messagebox.showerror(title="Error", message="No screenshot taken or copied image")
def textp():
    clr()
    try:
        global reader
        global out
        img = ImageGrab.grabclipboard()
        img.save('snip.png', 'PNG')
        file_name = "snip.png"
        output = reader.readtext(file_name)
        b = ''
        for a in output:
            b += a[1]
            b += ' '
        p(b)
    except:
        messagebox.showerror(title="Error", message="No screenshot taken or copied image")
def texts():
    clr()
    try:
        global reader
        global out
        img = ImageGrab.grabclipboard()
        img.save('snip.png', 'PNG')
        file_name = "snip.png"
        output = reader.readtext(file_name)
        b = ''
        for a in output:
            b += a[1]
            b += ' '
        s(b)
    except:
        messagebox.showerror(title="Error", message="No screenshot taken or copied image")
def g(b):
    out.insert(INSERT, b)
    s(b)
    p(b)
def s(b):
    url = "https://www.google.com.tr/search?q={}".format(b)
    webbrowser.open_new_tab(url)
    out.insert(INSERT, b)
def p(b):
    pyperclip.copy(b)
    pyperclip.paste()
    out.insert(INSERT, b)
global reader
reader = easyocr.Reader(['en'])
root = Tk()
logo = PhotoImage(file='logo.png')
root.configure(bg="black")
root.geometry("400x350")
root.title("Text Extracter")
root.iconphoto(False,logo)
Label(text="By s0ulix", bg="red", width="50", height="2", font=("Helvetica", 13), fg="white").pack()
Button(text="Copy+Search text", height="2", width="20", font=("Helvetica", 13), command=textg).pack()
Button(text="Copy text", height="2", width="20", font=("Helvetica", 13), command=textp).pack()
Button(text="Search text", height="2", width="20", font=("Helvetica", 13), command=texts).pack()
global out
out=Text(root,width=50,height=5)
out.pack()
root.mainloop()