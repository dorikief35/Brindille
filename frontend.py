from tkinter import *
from tkinter import filedialog
from Master import principale
import shutil 
import csv

##############################################################################################################################
def clearLogs ():
    txtarea.configure(state=NORMAL)
    open('logs.txt','w').close()
    txtarea.delete('1.0', END)
    txtarea.configure(state=DISABLED)

def watchfolder_button():
    global watchfolder_path
    filename = filedialog.askdirectory()
    watchfolder_path.set(filename)
    print(filename)

def xdcam_button():
    global xdcam_path
    filename = filedialog.askdirectory()
    xdcam_path.set(filename)
    print(filename)

def prores_button():
    global prores_path
    filename = filedialog.askdirectory()
    prores_path.set(filename)
    print(filename)

def invalid_button():
    global invalid_path
    filename = filedialog.askdirectory()
    invalid_path.set(filename)
    print(filename)

def getSavedPaths():
    global watchfolder_path
    global xdcam_path
    global prores_path
    global invalid_path
    
    # Ouverture du fichier csv
    with open("paths.csv",'r')as csvfile:
        reader = csv.reader(csvfile)
        row1 = next(reader)
        watchfolder_path.set(row1[0])
        xdcam_path.set(row1[1])
        prores_path.set(row1[2])
        invalid_path.set(row1[3])

def openFile():
    txtarea.configure(state=NORMAL)
    txtarea.delete('1.0', END)
    tf = 'logs.txt'
    tf = open(tf)
    data = tf.read()
    txtarea.insert(END, data)
    txtarea.see(END) # scroll to bottoms
    tf.close()
    txtarea.configure(state=DISABLED)
    getSavedPaths()

def start_button():
    # Send the paths to the main function
    principale(watchfolder_path.get(),xdcam_path.get(),prores_path.get(),invalid_path.get())

    # Open the logs file
    openFile()

##############################################################################################################################
#Styles
bgcolor = '#d9d9d9'

#Main window
root = Tk()
root.minsize(width=400, height=800)
root.configure(background= bgcolor)
root.title('Brindille')
root.iconbitmap("logoBrindille.ico")


#Variables
watchfolder_path = StringVar()
xdcam_path = StringVar()
prores_path = StringVar()
invalid_path = StringVar()

##############################################################################################################################
#Watchfolder
buttonWf = Button(text="Watchfolder ...", command=watchfolder_button)
buttonWf.pack(side=TOP,expand=YES,fill=BOTH, pady=10, padx=60)
lblwf = Label(master=root,textvariable=watchfolder_path,background=bgcolor)
lblwf.pack(side=TOP, expand=YES, fill=BOTH)

#Xdcam
buttonXd = Button(text="Xdcam ...", command=xdcam_button)
buttonXd.pack(side=TOP,expand=YES,fill=BOTH, pady=10, padx=60)
lblXd = Label(master=root,textvariable=xdcam_path,background=bgcolor)
lblXd.pack(side=TOP, expand=YES, fill=BOTH)

#Prores
buttonPro = Button(text="Prores ...", command=prores_button)
buttonPro.pack(side=TOP,expand=YES,fill=BOTH, pady=10, padx=60)
lblPro = Label(master=root,textvariable=prores_path,background=bgcolor)
lblPro.pack(side=TOP,expand=YES,fill=BOTH)

#Invalid
buttonInv = Button(text="Invalid ...", command=invalid_button)
buttonInv.pack(side=TOP,expand=YES,fill=BOTH, pady=10, padx=60)
lblInv = Label(master=root,textvariable=invalid_path,background=bgcolor)
lblInv.pack(side=TOP,expand=YES,fill=BOTH,)

#Compute
buttonCompute = Button(text="Compute", command=start_button,highlightthickness=10,highlightbackground="red")
buttonCompute.pack(side=TOP,expand=NO,fill=BOTH, padx=120, pady=10)

#Text area
txtarea = Text(root, width=40, height=20)
txtarea.configure(state=DISABLED)
txtarea.pack(side=TOP, expand=False, fill=X, padx=30, pady=10)

#Open file
openfile = Button(root, text="Refresh", command=openFile)
openfile.pack(side=TOP,expand=True, fill=X, padx=60, pady=10)

#Clear logs
buttonClear = Button(text="Clear logs", command=clearLogs)
buttonClear.pack(side=TOP, expand=True, fill=X, padx=120, pady=10)

root.mainloop()