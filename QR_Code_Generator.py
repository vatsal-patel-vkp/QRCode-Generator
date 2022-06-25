from tkinter import *
from tkinter import messagebox
import pyqrcode
import os

window = Tk()
window.geometry('650x650')
window.title('QR Code Generator')
window.resizable(0,0)


'''Definging Functions'''
def generate():
    if len(subject.get()) != 0:
        global myQr
        myQr = pyqrcode.create(subject.get())
        qrimage = myQr.xbm(scale= 6)
        global photo
        photo = BitmapImage(data= qrimage)
    else:
        messagebox.showinfo('Error', 'Please enter the subject')
    try:
        showcode()
    except:
        pass

def showcode():
    global photo
    notificationLabel.config(image= photo)

def save():
    dir = path1 = os.getcwd() + "\\QR Codes"   #Folder to save all the codes
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get()) != 0:
            qrimage = myQr.png(os.path.join(dir, name.get() + ".png"), scale= 6)
        else:
            messagebox.showinfo('Error', 'File name cannot be empty')
    except:
        messagebox.showinfo('Error', 'Please generate QR code')
        print(dir)
        print(qrimage)
        
def reset():
    subject.set("")
    name.set("")
    
    


headingframe = Frame(window, bg= '#FFBB00', bd= 5)
headingframe.place(relx= 0.1, rely= 0.03, relwidth= 0.8, relheight= 0.1)
headinglbl = Label(headingframe, text= 'QR Code Generator', bg='black', fg= 'white', font= 'Courier 15 bold')
headinglbl.place(relx= 0, rely= 0, relwidth= 1, relheight= 1)

displayframe = Frame(window, bg= 'black')
displayframe.place(relx= 0.1, rely= 0.15, relwidth= 0.8, relheight= 0.8)

'''Subject'''
subject = StringVar()
sublbl = Label(displayframe, text= 'Subject',bg= 'black', fg= 'white', font= 'Courier 12')
sublbl.place(relx=0.01, rely=0.05, relwidth=0.2, relheight= 0.07)
subbox = Entry(displayframe, textvariable= subject, font= 'Courier 12')
subbox.place(relx= 0.3, rely= 0.05, relwidth= 0.6, relheight= 0.07)

name = StringVar()
namelbl = Label(displayframe, text= 'Save As',bg= 'black', fg= 'white', font= 'Courier 12')
namelbl.place(relx=0.01, rely=0.15, relwidth=0.2, relheight= 0.07)
namebox = Entry(displayframe, textvariable= name, font= 'Courier 12')
namebox.place(relx= 0.3, rely= 0.15, relwidth= 0.6, relheight= 0.07)

notificationlbl = StringVar()
notificationLabel = Label(displayframe, bg= 'white')
notificationLabel.place(relx= 0.01, rely= 0.25, relwidth= 0.98, relheight= 0.4)


    

'''Button'''
qrcodebtn = Button(displayframe, text= 'Display QR Code', font= 'Courier 12', command= generate)
qrcodebtn.place(relx= 0.05, rely= 0.7, relwidth= 0.4, relheight= 0.1)

savebtn = Button(displayframe, text= 'Save', font= 'Courier 12', command= save)
savebtn.place(relx= 0.55, rely= 0.7, relwidth= 0.4, relheight= 0.1)

resetbtn = Button(displayframe, text= 'Reset', font= 'Courier 12', command= reset)
resetbtn.place(relx= 0.05, rely= 0.85, relwidth= 0.4, relheight= 0.1)

exitbtn = Button(displayframe, text= 'Exit', font= 'Courier 12', command= window.destroy)
exitbtn.place(relx= 0.55, rely= 0.85, relwidth= 0.4, relheight= 0.1)

'''
#Responsive Layout
totalrows = 3
totalcols = 3
for row in range(totalrows+1):
    window.grid_rowconfigure(row, weight= 1)
for col in range(totalcols+1):
    window.grid_columnconfigure(col, weight= 1)
'''



window.mainloop()