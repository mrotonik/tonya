from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np




osnova=Tk()

osnova.title("Графіки")
osnova.geometry('450x200')
tab_control = ttk.Notebook(osnova)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text='ВЕРТ. Е ПЛОЩИНА')
tab_control.add(tab2, text='ВЕРТ. Н ПЛОЩИНА')
tab_control.add(tab3, text='ГОР. Е ПЛОЩИНА')
tab_control.add(tab4, text='ВІЛЬНИЙ ПРОСТІР')
tab_control.pack(expand=2, fill='both')




def vetre():
    la = float(lam.get())#довжину хвилі
    h = float(h1.get())#h- висоти
    l = float(l1.get())#l
    k = 2 * np.pi / la
    theta = np.arange(0., 2., 1. / 180.) * np.pi / 2
    plt.polar(theta,((np.cos(k * l * np.cos(theta)) - np.cos(k * l)) / (np.sqrt(1 - np.cos(theta) * np.cos(theta)))) * (np.sin(k * h * np.sin(theta))))
    # plt.polar(theta, (((1 - np.cos(k * l)) * np.sin(k * h * np.sin(theta))) / np.sin(theta)))
    title1 = (f'ВЕРТИКАЛЬНА Е ПЛОЩИНА \n ' + f'h={h / la}* lambda')
    plt.title(title1)
    plt.show()


def vetrh():
    la = float(lam1.get())#довжину хвилі
    h = float(h11.get())#h- висоти
    l = float(l11.get())#l
    k = 2 * np.pi / la
    theta = np.arange(0., 2., 1. / 180.) * np.pi / 2
    plt.polar(theta, ((np.cos(k * l * np.cos(theta))) - np.cos(k * l)) * (np.sin(k * h * np.sin(theta))))
    title2 = 'ВЕРТИКАЛЬНА Н ПЛОЩИНА \n'  f'h={h / la}* lambda'
    plt.title(title2)
    plt.show()

def gore():
    bi = int(bi1.get())
    la = float(lam2.get())  # довжину хвилі
    h = float(h12.get())  # h- висоти
    l = float(l12.get())  # l
    k = 2 * np.pi / la
    theta = np.arange(0., 2., 1. / 180.) * np.pi
    plt.polar(theta, (((np.cos(k * l * np.cos(np.radians(bi)) * np.sin(theta))) - np.cos(k * l)) * np.sin(k * h * np.sin(bi))) / (np.sqrt(1 - pow(np.cos(np.radians(bi)), 2) * pow(np.sin(theta), 2))))
    title3 = 'ГОРИЗОНТАЛЬНА Е ПЛОЩИНА \n' f'h={h / la}* lambda'
    plt.title(title3)
    plt.show()

def vil():
    la = float(lam3.get())  # довжину хвилі
    #h = float(h13.get())  # h- висоти
    l = float(l13.get())  # l
    k = 2 * np.pi / la
    theta = np.arange(0., 2., 1. / 180.) * np.pi / 2
    plt.polar(theta, ((np.cos(k * l * np.cos(theta)) - np.cos(k * l)) / np.sin(theta)))
    title4 = 'ВІЛЬНИЙ ПРОСТІР \n'  f'l={l / la}* lambda'
    plt.title(title4)
    plt.show()


############################tab1#############
a1=Label(tab1,text='Введіть довжину хвилі:')
a1.config(font=('Verdana',10))
a1.place(x=15,y=25)
a2=Label(tab1,text='Введіть h:')
a2.config(font=('Verdana',10))
a2.place(x=15,y=75)
a3=Label(tab1,text='Введіть l:')
a3.config(font=('Verdana',10))
a3.place(x=15,y=125)
############################tab2#############
a12=Label(tab2,text='Введіть довжину хвилі:')
a12.config(font=('Verdana',10))
a12.place(x=15,y=25)
a2=Label(tab2,text='Введіть h:')
a2.config(font=('Verdana',10))
a2.place(x=15,y=75)
a3=Label(tab2,text='Введіть l:')
a3.config(font=('Verdana',10))
a3.place(x=15,y=125)
############################tab3#############
a1=Label(tab3,text='Введіть довжину хвилі:')
a1.config(font=('Verdana',10))
a1.place(x=15,y=25)
a2=Label(tab3,text='Введіть h:')
a2.config(font=('Verdana',10))
a2.place(x=15,y=75)
a3=Label(tab3,text='Введіть l:')
a3.config(font=('Verdana',10))
a3.place(x=15,y=125)
a4=Label(tab3,text='Введіть угол:')
a4.config(font=('Verdana',10))
a4.place(x=280,y=25)
bi1=Entry(tab3)#MODUL
bi1.place(x=380,y=25,width=40,height=20)
############################tab4#############
a1=Label(tab4,text='Введіть довжину хвилі:')
a1.config(font=('Verdana',10))
a1.place(x=15,y=25)
#a2=Label(tab4,text='Введіть h:')
#a2.config(font=('Verdana',10))
#a2.place(x=15,y=75)
a3=Label(tab4,text='Введіть l:')
a3.config(font=('Verdana',10))
a3.place(x=15,y=75)

##################################


lam=Entry(tab1)#MODUL
lam.place(x=230,y=50,width=40,height=20)

h1=Entry(tab1)#MODUL
h1.place(x=230,y=100,width=40,height=20)

l1=Entry(tab1)#MODUL
l1.place(x=230,y=150,width=40,height=20)


lam1=Entry(tab2)#MODUL
lam1.place(x=230,y=50,width=40,height=20)

h11=Entry(tab2)#MODUL
h11.place(x=230,y=100,width=40,height=20)

l11=Entry(tab2)#MODUL
l11.place(x=230,y=150,width=40,height=20)


lam2=Entry(tab3)#MODUL
lam2.place(x=230,y=50,width=40,height=20)

h12=Entry(tab3)#MODUL
h12.place(x=230,y=100,width=40,height=20)

l12=Entry(tab3)#MODUL
l12.place(x=230,y=150,width=40,height=20)



lam3=Entry(tab4)#MODUL
lam3.place(x=230,y=50,width=40,height=20)

#h13=Entry(tab4)#MODUL
#h13.place(x=230,y=100,width=40,height=20)

l13=Entry(tab4)#MODUL
l13.place(x=230,y=100,width=40,height=20)










b1= Button(tab1, text='Розрахувати',command=vetre)#knopk
b1.place(x=350,y=130,)

b2= Button(tab2, text='Розрахувати',command=vetrh)#knopk
b2.place(x=350,y=130,)

b3= Button(tab3, text='Розрахувати',command=gore)#knopk
b3.place(x=350,y=130,)

b4= Button(tab4, text='Розрахувати',command=vil)#knopk
b4.place(x=350,y=130,)


osnova.mainloop()