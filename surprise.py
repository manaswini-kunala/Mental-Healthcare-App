from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser
def sad():
    def blog():
        win.destroy()
        win1= Toplevel()
        #Define the geometry of the window
        win1.geometry("400x600")
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
        win.destroy()
        win1= Toplevel()
        #Define the geometry of the window
        win1.geometry("400x600")
        #Load the image
        def callback(url):
            webbrowser.open_new_tab(url)
        link = Label(win1, text="Video1",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link.place(x=20,y=50)
        link.bind("<Button-1>", lambda e:
        callback("https://www.counseling.txstate.edu/Self-Help---Resources/DigitalSelfHelpResources.html"))
        win1.mainloop()
    def audio():
        win.destroy()
        win1= Toplevel()
        #Define the geometry of the window
        win1.geometry("400x600")
        #Load the image
        def callback(url):
            webbrowser.open_new_tab(url)
        link = Label(win1, text="Video1",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link.place(x=20,y=50)
        link.bind("<Button-1>", lambda e:
        callback("https://www.counseling.txstate.edu/Self-Help---Resources/DigitalSelfHelpResources.html"))
        win1.mainloop()
    def video():
        win.destroy()
        win1= Toplevel()
        #Define the geometry of the window
        win1.geometry("400x600")
        #Load the image
        def callback(url):
            webbrowser.open_new_tab(url)
        link = Label(win1, text="Video1",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link.place(x=20,y=50)
        link.bind("<Button-1>", lambda e:
        callback("https://youtu.be/afoAXho6EHs"))
        win1.mainloop()
    win= Tk()
    button1 = Button(win,text="Video", bg='blue',command=video)
    button1.place(x=20,y=50)
    button2 = Button(win,text="Blogs", bg='Green',command=blog)
    button2.place(x=120,y=50)
    button3 = Button(win,text="Audio", bg='Yellow',command=audio)
    button3.place(x=20,y=120)
    button4 = Button(win,text="CBT", bg='red',command=cbt)
    button4.place(x=120,y=120)
    win.mainloop()

