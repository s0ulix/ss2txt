# ss2txt
This is a python script which will automatically extract text from the images which are copied in you clipboard or you can say the screenshots taken from snip tool in window 10
and also copied images from browser.
In the new feature now you can also select pictures from your computer.
There are 2 features in this script one is you can automatically copy the extracted text to your clipboard and the 2nd one is that it will automatically search the extracted text in your browser.

Same working ss2txt but works on easyocr python module doesn't need any tesseract installation but takes a lot of ram nearly 1 gb
But much more accurate, If you have ram to spare and some processing power to spare for the accuracy use the easyocr one.

Else use tesseract one

For Pytesseract:-

Download tesseract from https://drive.google.com/file/d/1pJ-h4ujrzgmU61cGyzltOvitv1kfDF3i/view?usp=sharing and install it to your system

Note:- If path related error o tesseract occurs add the path of tesseract exe in the script as per your system

Modules:

*webbrowser

*pytesseract

*PIL 

*tkinter 

*pyperclip

instally any module is as below

pip install module_name   (eg pip install pytesseract)


Dont forget to add both the png files in the same folder as of script.
