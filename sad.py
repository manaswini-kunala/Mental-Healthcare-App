from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser
def sad():
    def blog():

        win1= Toplevel()
        width = win1.winfo_screenwidth()
        height = win1.winfo_screenheight()
        win1.geometry("%dx%d" % (width, height))
        #Define the geometry of the window
        # win1.geometry("1000x1000")
        #Load the image
        def callback(url):
            webbrowser.open_new_tab(url)
        link = Label(win1, text="Blog1",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link.place(x=20,y=50)
        link.bind("<Button-1>", lambda e:
        callback("https://www.wikihow.com/Overcome-Sadness?amp=1"))
        link1 = Label(win1, text="Blog2",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link1.place(x=20,y=50)
        link1.bind("<Button-1>", lambda e:
        callback("https://www.gundersenhealth.org/health-wellness/live-happy/healthy-ways-to-deal-with-sadness/"))
        link2 = Label(win1, text="Blog3",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link2.place(x=20,y=50)
        link2.bind("<Button-1>", lambda e:
        callback("https://www.betterhealth.vic.gov.au/health/healthyliving/its-okay-to-feel-sad"))
        link3 = Label(win1, text="Blog4",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link3.place(x=20,y=50)
        link3.bind("<Button-1>", lambda e:
        callback("https://www.helpguide.org/articles/depression/coping-with-depression.htm"))
        link4 = Label(win1, text="Blog4",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link4.place(x=20,y=50)
        link4.bind("<Button-1>", lambda e:
        callback("https://thiswayup.org.au/learning-hub/depression-explained/"))
        win1.mainloop()
    def cbt():

        win1= Toplevel()
        width = win1.winfo_screenwidth()
        height = win1.winfo_screenheight()
        win1.geometry("%dx%d" % (width, height))
        #Define the geometry of the window
        # win1.geometry("400x600")
        #Load the image
        def callback(url):
            webbrowser.open_new_tab(url)
        link = Label(win1, text="CBT techniques",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link.place(x=20,y=50)
        link.bind("<Button-1>", lambda e:
        callback("https://www.counseling.txstate.edu/Self-Help---Resources/DigitalSelfHelpResources.html"))
        win1.mainloop()
    def audio():

        win1= Toplevel()
        width = win1.winfo_screenwidth()
        height = win1.winfo_screenheight()
        win1.geometry("%dx%d" % (width, height))
        #Define the geometry of the window
        # win1.geometry("400x600")
        #Load the image
        def callback(url):
            webbrowser.open_new_tab(url)
        link = Label(win1, text="Audio",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link.place(x=20,y=50)
        link.bind("<Button-1>", lambda e:
        callback("https://www.counseling.txstate.edu/Self-Help---Resources/DigitalSelfHelpResources.html"))
        win1.mainloop()
    def video():

        win1= Toplevel()
        width = win1.winfo_screenwidth()
        height = win1.winfo_screenheight()
        win1.geometry("%dx%d" % (width, height))
        #Define the geometry of the window
        # win1.geometry("400x600")
        #Load the image
        def callback(url):
            webbrowser.open_new_tab(url)
        link = Label(win1, text="Video1",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link.place(x=20,y=50)
        link.bind("<Button-1>", lambda e:
        callback("https://youtu.be/afoAXho6EHs"))
        win1.mainloop()
    win= Tk()
    width = win.winfo_screenwidth()
    height = win.winfo_screenheight()
    win.geometry("%dx%d" % (width, height))
    la = Label(win, text="Resources", font=('algerian', 15, 'bold'))
    la.place(x=600, y=100)
    button1 = Button(win, text="Video", bg='light blue', width=20, height=10, command=video)
    button1.place(x=520, y=150)
    button2 = Button(win, text="Blogs", bg='light green', width=20, height=10, command=blog)
    button2.place(x=680, y=150)
    button3 = Button(win, text="Audio", bg='light green', width=20, height=10, command=audio)
    button3.place(x=520, y=320)
    button4 = Button(win, text="CBT", bg='light blue', width=20, height=10, command=cbt)
    button4.place(x=680, y=320)
    win.mainloop()

