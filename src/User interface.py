
from tkinter import *
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image
import pytesseract

"""
app = []
main = Tk()
main.title("Handwritten English Word Recognition")
main.geometry("600x400+40+30")
Label(main, text="Handwritten English Word Recognition", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black", fg="White").pack()
Label(main, text="", bg='#174873', width='600', height='400').pack()


def download():
    global screen
    screen = Toplevel(main)
    screen.title("Browse")
    screen.geometry("600x400+40+30")
    Label(screen, text="Browse", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black",
          fg="White").pack()
    Label(screen, text="", bg='#174873', width='600', height='400').pack()
    category = Button(screen, text="Category Wise", command=categorywise).place(x=260, y=100)
    no.ofdownloads = Button(screen, text="No. of Downloads", command=nod).place(x=260, y=150)
    App = Button(screen, text="App", command=app).place(x=260, y=200)
    Button(screen, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',
           command=screen.destroy).place(x=425, y=350)  # button to navigate back


def categorywise():
    global c
    c = Toplevel(screen)
    c.title("Category Wise")
    c.geometry("600x400+40+30")
    Label(c, text="Category Wise", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black", fg="White").pack()
    Label(c, text="", bg='#174873', width='600', height='400').pack()
    md = Button(c, text="Max Download", command=maxdownload).place(x=260, y=100)
    dowds = Button(c, text="Downloads", command=downloads).place(x=260, y=150)
    downtrend = Button(c, text="Download Trend", command=downloadtrend).place(x=260, y=200)
    rat = Button(c, text="Ratings", command=ratings).place(x=260, y=250)
    Button(c, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white', command=c.destroy).place(
        x=425, y=350)


def maxdownload():
    global window1
    window1 = Toplevel(c)
    window1.title("Maxdownload")
    window1.geometry("600x400+40+30")
    Label(window1, text="Maximum Download", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black",
          fg="White").pack()
    Label(window1, text="", bg='#174873', width='600', height='400').pack()
    Button(window1, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',
           command=window1.destroy).place(x=425, y=350)


def downloads():
    global window2
    window2 = Toplevel(c)
    window2.title("Browse")
    window2.geometry("600x400+40+30")
    Label(window2, text="Browse", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black",
          fg="White").pack()
    Label(window2, text="", bg='#174873', width='600', height='400').pack()
    Button(window2, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',
           command=window2.destroy).place(x=425, y=350)


def downloadtrend():
    global window3
    window3 = Toplevel(c)
    window3.title("DownloadTrend")
    window3.geometry("600x400+40+30")
    Label(window3, text="Download Trend", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black",
          fg="White").pack()
    Label(window3, text="", bg='#174873', width='600', height='400').pack()
    Button(window3, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',
           command=window3.destroy).place(x=425, y=350)


def ratings():
    global window4
    window4 = Toplevel(c)
    window4.title("Ratings")
    window4.geometry("600x400+40+30")
    Label(window4, text="Ratings", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black", fg="White").pack()
    Label(window4, text="", bg='#174873', width='600', height='400').pack()
    Button(window4, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',
           command=window4.destroy).place(x=425, y=350)


def nod():
    global no
    no = Toplevel(screen)
    no.title("No. of Downloads")
    no.geometry("600x400+40+30")
    Label(no, text="No. of Downloads", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black",
          fg="White").pack()
    Label(no, text="", bg='#174873', width='600', height='400').pack()
    Button(no, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white', command=no.destroy).place(
        x=425, y=350)


def app():
    global ap
    ap = Toplevel(screen)
    ap.title("App")
    ap.geometry("600x400+40+30")
    Label(ap, text="App", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black", fg="White").pack()
    Label(ap, text="", bg='#174873', width='600', height='400').pack()
    per = Button(ap, text="Percentage", command=percentage).place(x=260, y=100)
    stuapp = Button(ap, text="Study App", command=studyapp).place(x=260, y=150)
    Button(ap, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white', command=ap.destroy).place(
        x=425, y=350)


def percentage():
    global window5
    window5 = Toplevel(ap)
    window5.title("Percentage")
    window5.geometry("600x400+40+30")
    Label(window5, text="Percentage", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black",
          fg="White").pack()
    Label(window5, text="", bg='#174873', width='600', height='400').pack()
    Button(window5, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',
           command=window5.destroy).place(x=425, y=350)


def studyapp():
    global window6
    window6 = Toplevel(ap)
    window6.title("Studyapp")
    window6.geometry("600x400+40+30")
    Label(window6, text="Study App", width="500", height="2", font=("Calibri", 22, 'bold'), bg="black",
          fg="White").pack()
    Label(window6, text="", bg='#174873', width='600', height='400').pack()
    Button(window6, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',
           command=window6.destroy).place(x=425, y=350)


dload = Button(main, text="Browse", command=download).place(x=260, y=100)
Button(main, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white', command=main.destroy).place(x=425, y=350)
"""
root = Tk()
def readFimage():
    path = PathTextBox.get('1.0', 'end-1c')
    if path:
        im = Image.open(path)
        from main import main
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        #text = pytesseract.image_to_string(im, lang='eng')
        ResultTextBox.delete('1.0', END)
        ResultTextBox.insert(END,main())
    else:
        ResultTextBox.delete('1.0', END)
        ResultTextBox.insert(END, "FILE CANNOT BE READ")


def OpenFile():
    name = askopenfilename(initialdir="/",
                           filetypes=(("PNG File", "*.png"), ("BMP File", "*.bmp"), ("JPEG File", "*.jpeg")),
                           title="Choose a file."
                           )
    PathTextBox.delete("1.0", END)
    PathTextBox.insert(END, name)

Title = root.title("Image Reader!")
path = StringVar()
HeadLabel1 = Label(root, text="Image ")
HeadLabel1.grid(row=1, column=1, sticky=(E))
HeadLabel2 = Label(root, text=" Reader")
HeadLabel2.grid(row=1, column=2, sticky=(W))

InputLabel = Label(root, text="INPUT IMAGE:")
InputLabel.grid(row=2, column=1)

BrowseButton = Button(root, text="Browse", command=OpenFile)
BrowseButton.grid(row=2, column=2)

PathLabel = Label(root, text="Path:")
PathLabel.grid(row=3, column=1, sticky=(W))

PathTextBox = Text(root, height=2)
PathTextBox.grid(row=4, column=1, columnspan=2)

ReadButton = Button(root, text="READ FROM IMAGE", command=readFimage)
ReadButton.grid(row=5, column=2)

DataLabel = Label(root, text="DATA IN IMAGE:")
DataLabel.grid(row=6, column=1, sticky=(W))

ResultTextBox = Text(root, height=6)
ResultTextBox.grid(row=7, column=1, columnspan=2)

root.mainloop()
#main.mainloop()


