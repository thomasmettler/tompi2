import piplates.DAQCplate as DAQC 
import RPi.GPIO as GPIO
import time
from Tkinter import *
import tkFont

def task(): 
    global lastT
    global lastR
    global lastSW
    global swMode 
    global GC
    adata=DAQC.getADCall(3)
    val=round(DAQC.getADC(0,8),1)
    Power5Text.set(val)
    
    val=round((adata[1]-2.73)*100,2)
    val=0.2*val+0.8*lastT
    lastT=val
    TempText.set(str("{:>3.1f}".format(val))+'C')
    
    val=round(adata[2]*12.21/1.636,1)
    Power12Text.set(val)
    
    val=round(adata[0]/4.096*100,1)  
    FanText.set(str(val)+'%')
    DAQC.setPWM(0,0,int(val*1024/100))
    
    val=DAQC.getRANGE(0,6,'c')
    if isinstance(val,float):
        if val>100:
            val=99.9 
    else:
        val=0
    val=round(val,1)
    val=0.8*lastR+0.2*val
    lastR=val
    RangeText.set(str("{:>2.1f}".format(val))+'cm')
      
    lamp=0
    if(DAQC.getDINbit(0,2)==1):
        lamp=32

    sw=DAQC.getSWstate(0)
    if (sw==1) and (lastSW==0):
        lastSW=1
        swMode = not swMode
	if swMode:
            GCmode.set('Binary Code :')
        else:
            GCmode.set('Grey Code :')
    if (sw==0) and (lastSW==1):
        lastSW=0    


    val=(int(adata[7]*32/4.096))
    if swMode == 0:
        GCText.set(GC[val])
        num=GC[val]
    else:
        GCText.set(val)
        num=val
    DAQC.setDOUTall(0,(num+lamp))   
       
    root.after(100,task)

def shutdown():
    DAQC.CLOSE()
    root.destroy() 
    root.quit()

    
root = Tk()
root.config(bg="black")
root.attributes("-fullscreen", True)

#swidth=root.winfo_screenwidth()
#sheight=root.winfo_screenheight()
         
##Create Fonts
big = tkFont.Font(family='Helvetica', size=100, weight='bold')
title = tkFont.Font(family='Helvetica', size=60, weight='bold') 
heading = tkFont.Font(family='Helvetica', size=55, weight='bold')        
normal = tkFont.Font(family='Helvetica', size=20, weight='bold') 

##Create Gray Code
GC=[0x00,0x01,0x03,0x02,0x06,0x07,0x05,0x04,0x0C,0x0D,0x0F,0x0E,0x0A,0x0B,0x09,0x08,0x18,0x19,0x1B,0x1A,0x1E,0x1F,0x1D,0x1C,0x14,0x15,0x17,0x16,0x12,0x13,0x11,0x10]


tf=Frame(root,padx=4,pady=4,bd=2,relief='sunken',bg='#000000888').grid(row=2,column=0,sticky=E+W+N+S)
logo = PhotoImage(file = '3D-ppLogo-WIDE.gif')
pp=Label(tf,image=logo,bg="White").grid(row=0,column=0,columnspan=2)  
Label(tf, text="DAQCplate Data Acquisition and Control", bg='White',fg='#000888000',font=title,anchor=CENTER).grid(row=1,column=0,columnspan=2,sticky=E+W)

lastSW=1
lastMode=0
swMode=0
lastT=25

TempText=StringVar()
TempText.set('25') 
Label(tf, text="Temperature: ", bg='#000000888',fg='White',font=big,anchor=E).grid(row=2,column=0,sticky=E+W)
Label(tf, textvariable=TempText, bg='#000000888',fg='White',font=big,anchor=W).grid(row=2,column=1,sticky=E+W)

lastR = 140
RangeText=StringVar()
RangeText.set('0.0')
Label(tf, text="Range: ", bg='#000888000',fg='White',font=big,anchor=E).grid(row=3,column=0,sticky=E+W)
Label(tf, textvariable=RangeText, bg='#000888000',fg='White', font=big,anchor=W).grid(row=3,column=1,sticky=W+E)

FanText=StringVar()
FanText.set('0.0')
Label(tf, text="Fan Speed: ", bg='#888000000',fg='White',font=big,anchor=E).grid(row=4,column=0,sticky=E+W)
Label(tf, textvariable=FanText, bg='#888000000',fg='White', font=big,anchor=W).grid(row=4,column=1,sticky=W+E)

Power5Text=StringVar()
Power12Text=StringVar()
GCText=StringVar()
GCText.set('0')
GCmode=StringVar()
GCmode.set('Grey Code :')
Label(tf, text="5VDC Voltage: ", bg='#888888000',fg='White',font=heading,anchor=E).grid(row=6,column=0,sticky=E+W)
Label(tf, textvariable=Power5Text, bg='#888888000',fg='White', font=heading,anchor=W).grid(row=6,column=1,sticky=W+E)
Label(tf, text="12VDC Voltage: ", bg='#888000888',fg='White',font=heading,anchor=E).grid(row=7,column=0,sticky=E+W)
Label(tf, textvariable=Power12Text, bg='#888000888',fg='White', font=heading,anchor=W).grid(row=7,column=1,sticky=W+E)
Label(tf, textvariable=GCmode, bg='#000888888',fg='White',font=heading,anchor=E).grid(row=5,column=0,sticky=E+W)
Label(tf, textvariable=GCText, bg='#000888888',fg='White', font=heading,anchor=W).grid(row=5,column=1,sticky=W+E)
close_button = Button(tf, text="X", command=shutdown).grid(row=7,column=1,sticky=E)
 
root.wm_protocol("WM_DELETE_WINDOW", shutdown) 
root.after(100,task)
root.mainloop()