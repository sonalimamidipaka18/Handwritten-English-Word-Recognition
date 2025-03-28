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
main.title("Handwritten Text Recognition")
main.geometry("600x400+40+30")
Label(main,text="Text Image", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
Label(main, text="", bg='#174873',width='600', height='400').pack()

Cm=Button(main,text="Recognized Image",width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=cm).place(x=430,y=350)

def cm():
   global screen
   screen = Toplevel(main)
   screen.title("converted image ")
   screen.geometry("600x400+40+30")
   Label(screen,text="Recognized Image", width="500", height="2", font=("Calibri", 22, 'bold'),bg="black",fg="White").pack()
   Label(screen, text="", bg='#174873',width='600', height='400').pack()
   
   Button(screen, text='Back', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=screen.destroy).place(x=425, y=350)

main.mainloop()