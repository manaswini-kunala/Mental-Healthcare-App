from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import webbrowser
def happy():
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
        callback("https://www.mhanational.org/31-tips-boost-your-mental-health"))
        link1 = Label(win1, text="Blog2",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link1.place(x=20,y=50)
        link1.bind("<Button-1>", lambda e:
        callback("https://www.happycounts.org/blog/the-link-between-mental-stability-happiness"))
        link2 = Label(win1, text="Blog3",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link2.place(x=20,y=50)
        link2.bind("<Button-1>", lambda e:
        callback("https://www.helpguide.org/articles/mental-health/cultivating-happiness.htm"))
        link3 = Label(win1, text="Blog4",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link3.place(x=20,y=50)
        link3.bind("<Button-1>", lambda e:
        callback("https://www.businessinsider.in/science/health/how-to-feel-happier-according-to-neuroscientists-and-psychologists/articleshow/59548742.cms"))
        link4 = Label(win1, text="Blog4",font=('Helveticabold', 15), fg="blue", cursor="hand2")
        link4.place(x=20,y=50)
        link4.bind("<Button-1>", lambda e:
        callback("https://maxweigand.medium.com/the-science-of-happiness-what-actually-makes-us-happy-78edcc9bdd58"))
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
        callback("https://youtu.be/ZbZSe6N_BXs"))
        win1.mainloop()
    win= Tk()
    width=win.winfo_screenwidth()
    height = win.winfo_screenheight()
    win.geometry("%dx%d" % (width,height))
    la = Label(win, text="Resources", font=('algerian', 15, 'bold'))
    la.place(x=600, y=100)
    button1 = Button(win,text="Video", bg='light blue',width=20,height=10,command=video)
    button1.place(x=520,y=150)
    button2 = Button(win,text="Blogs", bg='light green',width=20,height=10,command=blog)
    button2.place(x=680,y=150)
    button3 = Button(win,text="Audio", bg='light green',width=20,height=10,command=audio)
    button3.place(x=520,y=320)
    button4 = Button(win,text="CBT", bg='light blue',width=20,height=10,command=cbt)
    button4.place(x=680,y=320)
    win.mainloop()

