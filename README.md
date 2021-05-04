# ss2txt

There are 2 scripts for this program each having different module for OCR

One with easyocr which supports the hindi language with other languages but usage a lot of ram(ss2txt,py)

Other one is with tesseract which is good for english and use a very less ram.(ss2txt_pyt.py)

This is a python script which will automatically extract text from the images which are copied in you clipboard or you can say the screenshots taken from snip tool in window 10
and also copied images from browser.
In the new feature now you can also select pictures from your computer.
There are 2 features in this script one is you can automatically copy the extracted text to your clipboard and the 2nd one is that it will automatically search the extracted text in your browser.


Before using this script, You will need python installed and all the modules used here installed in your system.

Modules:

*webbrowser

*easyocr 

*PIL 

*tkinter 

*pyperclip

When you will run it for the first time one language package will install so wait for that (this is a one time thing so no worries).


Note:- Person having nvidia gpu install pytorch version which support cuda cores, torch version 1.5.0+cu92 is recomended
Which can be installed from this command

pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html
