import webbrowser
import easyocr
from PIL import ImageGrab
from tkinter import *
from tkinter import messagebox
import pyperclip
from tkinter.filedialog import askopenfilename
def clr():
    out.delete('1.0', END)
def textg(ch):
	@@ -16,16 +19,13 @@ def textg(ch):
            file_name = "snip.png"
        else:
            file_name=ch
        output = reader.readtext(file_name)
        b = ''
        for a in output:
            b += a[1]
            b += ' '
        return b
    except Exception as ex:
        messagebox.showerror(title="Error", message="No screenshot taken or copied image")
        print(ex)
        return None
def fi():
    file = askopenfilename(filetypes=[("image", ".jpeg"),("image", ".png"),("image", ".jpg"),])
    b=textg(file)
	@@ -65,22 +65,56 @@ def s2():
def s3():
    b=fi()
    cpy(b)
global reader
reader = easyocr.Reader(['en'])
root = Tk()
logo = PhotoImage(file='logo.png')
root.configure(bg="black")
root.geometry("400x450")
root.title("Text Extracter")
root.iconphoto(False,logo)
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
