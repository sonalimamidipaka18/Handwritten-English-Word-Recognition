from tkinter import Tk
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import tree

import seaborn as sns
from sklearn.metrics import r2_score
import statsmodels.api as sm

app=[]
main=Tk()
main.title("WELCOME TO THE DATA ANALYSIS OF THE APP")
main.geometry("600x400+40+30")
Label(main,text="DATA ANALYSIS", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
Label(main, text="", bg='#174873',width='600', height='400').pack()


dload=Button(main,text="DOWNLOAD",command=download).place(x=260,y=100)
predict=Button(main,text="PREDICTION",command=prediction).place(x=260,y=150)
coretion=Button(main,text="CO-RELATION",command=corelation).place(x=255,y=200)
senti=Button(main,text="SENTIMENTS",command=sentiments).place(x=255,y=250)
inface=Button(main,text="INTERFACE",command=interface).place(x=265,y=300)
Button(main, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=main.destroy).place(x=425, y=350)

def download():
    global screen
    screen= Toplevel(main)
    screen.title("downloads")
    screen.geometry("600x400+40+30")
    Label(screen,text="Downloads", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(screen, text="", bg='#174873',width='600', height='400').pack()
    category=Button(screen,text="Category Wise",command= categorywise).place(x=260,y=100)
    no.ofdownloads=Button(screen,text="No. of Downloads",command=nod).place(x=260,y=150)
    App=Button(screen,text="App",command=app).place(x=260,y=200)
    Button(screen, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=screen.destroy).place(x=425, y=350)#button to navigate back 
    
def categorywise():
   global c 
   c = Toplevel(screen)
   c.title("Category Wise")
   c.geometry("600x400+40+30")
   Label(c,text="Category Wise", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
   Label(c, text="", bg='#174873',width='600', height='400').pack()
   md=Button(c,text="Max Download",command=maxdownload).place(x=260,y=100)
   dowds=Button(c,text="Downloads",command=downloads).place(x=260,y=150)
   downtrend=Button(c,text="Download Trend",command=downloadtrend).place(x=260,y=200)
   rat=Button(c,text="Ratings",command=ratings).place(x=260,y=250)
   Button(c, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=c.destroy).place(x=425, y=350)
def maxdownload():
    global window1
    window1= Toplevel(c)
    window1.title("Maxdownload")
    window1.geometry("600x400+40+30")
    Label(window1,text="Maximum Download", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(window1, text="", bg='#174873',width='600', height='400').pack()
    Button(window1, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=window1.destroy).place(x=425, y=350)
def downloads():
    global window2
    window2 = Toplevel(c)
    window2.title("Downloads")
    window2.geometry("600x400+40+30")
    Label(window2,text="Downloads", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(window2, text="", bg='#174873',width='600', height='400').pack()
    Button(window2, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=window2.destroy).place(x=425, y=350)
    
def downloadtrend():
    global window3
    window3 = Toplevel(c)
    window3.title("DownloadTrend")
    window3.geometry("600x400+40+30")
    Label(window3,text="Download Trend", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(window3, text="", bg='#174873',width='600', height='400').pack()
    Button(window3, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=window3.destroy).place(x=425, y=350)

def ratings():
    global window4
    window4 = Toplevel(c)
    window4.title("Ratings")
    window4.geometry("600x400+40+30")
    Label(window4,text="Ratings", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(window4, text="", bg='#174873',width='600', height='400').pack()
    Button(window4, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=window4.destroy).place(x=425, y=350)

def nod():
    global no 
    no = Toplevel(screen)
    no.title("No. of Downloads")
    no.geometry("600x400+40+30")
    Label(no,text="No. of Downloads", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(no, text="", bg='#174873',width='600', height='400').pack()
    Button(no, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=no.destroy).place(x=425, y=350)   

def app():
    global ap
    ap = Toplevel(screen)
    ap.title("App")
    ap.geometry("600x400+40+30")
    Label(ap,text="App", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(ap, text="", bg='#174873',width='600', height='400').pack()
    per=Button(ap,text="Percentage",command=percentage).place(x=260,y=100)
    stuapp=Button(ap,text="Study App",command=studyapp).place(x=260,y=150)
    Button(ap, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=ap.destroy).place(x=425, y=350)
def percentage():
    global window5
    window5= Toplevel(ap)
    window5.title("Percentage")
    awindow5.geometry("600x400+40+30")
    Label(window5,text="Percentage", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(window5, text="", bg='#174873',width='600', height='400').pack()
    Button(window5, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=window5.destroy).place(x=425, y=350)

def studyapp():
    global window6
    window6= Toplevel(ap)
    window6.title("Studyapp")
    window6.geometry("600x400+40+30")
    Label(window6,text="Study App", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(window6, text="", bg='#174873',width='600', height='400').pack()
    Button(window6, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=window6.destroy).place(x=425, y=350)

def prediction():
    global screen1
    screen1= Toplevel(main)
    screen1.title("prediction")
    screen1.geometry("600x400+40+30")
    Label(screen1,text="Prediction", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(screen1, text="", bg='#174873',width='600', height='400').pack()
    coa=Button(screen1,text="Category of App",command= categoryofapp).place(x=260,y=100)
    bf=Button(screen1,text="10 Best foods for you",command=bestfoods).place(x=260,y=150)
    s=Button(screen1,text="Size of the App",command=sizeapp).place(x=260,y=200)
    Button(screen1, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=screen1.destroy).place(x=425, y=350)

def categoryofapp():
   global co 
   co=Toplevel(screen1)
   co.title("Category of App")
   co.geometry("600x400+40+30")
   Label(co,text="Category of App", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
   Label(co, text="", bg='#174873',width='600', height='400').pack()
   mostdown=Button(co,text="Mostly Download",command=mosltydownload).place(x=260,y=100)
   Button(co, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=co.destroy).place(x=425, y=350)
def mosltydownload():
   global window7
   window7= Toplevel(co)
   window7.title("Mostlyownload")
   window7.geometry("600x400+40+30")
   Label(window7,text="Mostly Downloaded", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
   Label(window7, text="", bg='#174873',width='600', height='400').pack()
   Button(window7, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=window7.destroy).place(x=425, y=350)

def bestfoods():
    global co
    co= Toplevel(screen1)
    co.title("10 bestfoods")
    co.geometry("600x400+40+30")
    Label(co,text="10 Bestfoods for you", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(co, text="", bg='#174873',width='600', height='400').pack()
    Button(co, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=co.destroy).place(x=425, y=350)

def sizeapp():
    global co
    co= Toplevel(screen1)
    co.title("Sizeofapp")
    co.geometry("600x400+40+30")
    Label(co,text="Size of the app", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(co, text="", bg='#174873',width='600', height='400').pack()
    Button(co, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=co.destroy).place(x=425, y=350)


def corelation():
    global screen2
    screen2= Toplevel(main)
    screen2.title("corelation")
    screen2.geometry("600x400+40+30")
    Label(screen2,text="Co-Relation", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(screen2, text="", bg='#174873',width='600', height='400').pack()
    down_rat=Button(screen2,text="Downloads and Ratings",command=downrat).place(x=225,y=100)
    sentpo_sentsub=Button(screen2,text="Sentiment Polarity and Sentiment Subjectivity",command=sentposub).place(x=180,y=150)
    Button(screen2, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=screen2.destroy).place(x=425, y=350)#button to navigate back           
def downrat():
    global dr 
    dr = Toplevel(screen2)
    dr.title("Downloads and Ratings")
    dr.geometry("600x400+40+30")
    Label(dr,text="Downloads and Ratings", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(dr, text="", bg='#174873',width='600', height='400').pack()
    Button(dr, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=dr.destroy).place(x=425, y=350)   
def sentposub():
    global sps 
    sps = Toplevel(screen2)
    sps.title("Sentiment Polarity and Subjectivity")
    sps.geometry("600x400+40+30")
    #Label(sps,text="Sentiment Polarity and Subjectivity", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    #Label(sps, text="", bg='#174873',width='600', height='400').pack()
    #Button(sps, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=sps.destroy).place(x=425, y=350)   
    #logic
    data2=pd.read_csv("C:\\pyproject\\Internship-project-Dataset2.csv")
    figure=plt.Figure(figsize=(12,6),dpi=100)
    ax=figure.add_subplot(111)
    ax.scatter(data2['Sentiment_Polarity'],data2['Sentiment_Subjectivity'],c='violet')
    scatter3=FigureCanvasTkAgg(figure,sps)
    scatter3.get_tk_widget().pack(side=tk.LEFT,fill=tk.BOTH)
    ax.legend()
    ax.set_xlabel("SENTIMENT POLARITY OF APPS")
    ax.set_ylabel("SENTIMENT SUBJECTIVITY OF APPS")

def sentiments():
    global screen3
    screen3= Toplevel(main)
    screen3.title("sentiments")
    screen3.geometry("600x400+40+30")
    Label(screen3,text="Sentiments", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(screen3, text="", bg='#174873',width='600', height='400').pack()
    mot=Button(screen3,text="Most",command=most).place(x=260,y=100)
    neutl=Button(screen3,text="Neutral",command=neutral).place(x=260,y=150)
    Button(screen3, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=screen3.destroy).place(x=425, y=350)#button to navigate back           
def most():
    global mt 
    mt = Toplevel(screen3)
    mt.title("Most Sentiments")
    mt.geometry("600x400+40+30")
    Label(mt,text="Most Sentiments", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(mt, text="", bg='#174873',width='600', height='400').pack()
    Button(mt, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=mt.destroy).place(x=425, y=350)   
def neutral():
    global neu 
    neu = Toplevel(screen3)
    neu.title("Neutral Sentiments")
    neu.geometry("600x400+40+30")
    Label(neu,text="Neutral Sentiments", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(neu, text="", bg='#174873',width='600', height='400').pack()
    Button(neu, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=neu.destroy).place(x=425, y=350)   


def interface():
    global screen4 
    screen4 = Toplevel(main)
    screen4.title("Interface")
    screen4.geometry("600x400+40+30")
    Label(screen4,text="Interface", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(screen4, text="", bg='#174873',width='600', height='400').pack()
    ndata=Button(screen4,text="NewData",command=newdata).place(x=260,y=100)
    rev=Button(screen4,text="Reviews",command=reviews).place(x=260,y=150)
    Button(screen4, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=screen4.destroy).place(x=425, y=350)   
def newdata():
    global nd 
    nd = Toplevel(screen4)
    nd.title("Add NewData")
    nd.geometry("600x400+40+30")
    Label(nd,text="Add NewData", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(nd, text="", bg='#174873',width='600', height='400').pack()
    Button(nd, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=nd.destroy).place(x=425, y=350)   
def reviews():
    global rv 
    rv = Toplevel(screen4)
    rv.title("Reviews")
    rv.geometry("600x400+40+30")
    Label(rv,text="Reviews", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
    Label(rv, text="", bg='#174873',width='600', height='400').pack()
    Button(rv, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=rv.destroy).place(x=425, y=350)   



main.mainloop()

