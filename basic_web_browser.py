# very basic web browser in python
import webbrowser
from tkinter import *
def google():
    webbrowser.open('http://www.google.com',new= 0, outoraise = True)
def amazon():
    webbrowser.open('http://www.amazon.com',new= 0, outoraise = True)
def instagram():
    webbrowser.open('http://www.instgram.com',new= 0, outoraise = True)
def github():
    webbrowser.open('http://www.github.com',new= 0, outoraise = True)
def youtube():
    webbrowser.open('http://www.youtube.com',new= 0, outoraise = True)
def twitter():
    webbrowser.open('http://www.twitter.com',new= 0, outoraise = True)
root = Tk()
root.geometry('350x150')
root.title('Mini Browser')
root.configure(background='white')
root.resizable(0,0)
btn0 = Button(root,text="Google",font=('arial',10,'bold')width=10,command=google).place(x=20,y=20)
btn1 = Button(root,text="Amazon",font=('arial',10,'bold')width=10,command=amazon).place(x=20,y=60)
btn2 = Button(root,text="Instagram",font=('arial',10,'bold')width=10,command=instagram).place(x=120,y=60)
btn3 = Button(root,text="Github",font=('arial',10,'bold')width=10,command=github).place(x=120,y=60)
btn4 = Button(root,text="YouTube",font=('arial',10,'bold')width=10,command=youtube).place(x=220,y=20)
btn5 = Button(root,text="Twitter",font=('arial',10,'bold')width=10,command=twitter).place(x=220,y=60)
root.mainloop()