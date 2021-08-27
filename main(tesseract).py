import pytesseract
import webbrowser
from PIL import ImageGrab
from PIL import Image as IMG
from tkinter import *
import pyperclip
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
def clr():
    out.delete('1.0', END)
def textg(ch):
    clr()
    try:
        if(ch==1):
            img = ImageGrab.grabclipboard()
            img.save('snip.png', 'PNG')
            file_name = "snip.png"
        else:
            file_name=ch
        b=pytesseract.image_to_string(IMG.open(file_name))
        return b
    except Exception as ex:
        messagebox.showerror(title="Error", message="No screenshot taken or copied image")
        print(ex)
        return None

def fi():
    file = askopenfilename(filetypes=[("image", ".jpeg"),("image", ".png"),("image", ".jpg"),])
    b=textg(file)
    return b
def cpysr(b):
    if(b!=None):
        out.insert(INSERT, b)
        url = "https://www.google.com.tr/search?q={}".format(b)
        webbrowser.open_new_tab(url)
        pyperclip.copy(b)
        pyperclip.paste()
def ser(b):
    if (b != None):
        url = "https://www.google.com.tr/search?q={}".format(b)
        webbrowser.open_new_tab(url)
        out.insert(INSERT, b)
def cpy(b):
    if (b != None):
        pyperclip.copy(b)
        pyperclip.paste()
        out.insert(INSERT, b)
def p1():
    b=textg(1)
    cpysr(b)
def p2():
    b = textg(1)
    ser(b)
def p3():
    b = textg(1)
    cpy(b)
def s1():
    b=fi()
    cpysr(b)
def s2():
    b=fi()
    ser(b)
def s3():
    b=fi()
    cpy(b)
root = Tk()
#logo = PhotoImage(file='logo.png')
root.configure(bg="black")
root.geometry("400x450")
root.title("Text Extracter")
#root.iconphoto(False,logo)
Label(text="By s0ulix", bg="red", width="50", height="2", font=("Helvetica", 13), fg="white").pack()
Button(text="Copy+Search text", height="2", width="30", font=("Helvetica", 13), command=p1).pack()
Button(text="Search text", height="2", width="30", font=("Helvetica", 13), command=p2).pack()
Button(text="Copy text", height="2", width="30", font=("Helvetica", 13), command=p3).pack()
Button(text="Select image(Search+Copy text)", height="2", width="30", font=("Helvetica", 13), command=s1).pack()
Button(text="Select image(Search text)", height="2", width="30", font=("Helvetica", 13), command=s2).pack()
Button(text="Select image(Copy text)", height="2", width="30", font=("Helvetica", 13), command=s3).pack()
global out
out=Text(root,width=50,height=5)
out.pack()
root.mainloop()
