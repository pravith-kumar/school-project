import socket
import tkinter
from tkinter import *
from tkinter import messagebox,filedialog
from PIL import Image
from tkinter import ttk
import time
choose,con,client,medium=None,None,None,None
def server():
     global con,client,choose,medium
     server = socket.socket()
     #host = socket.gethostname()
     #host = socket.gethostbyname(host)
     host='127.0.0.1'
     port = 1244
     server.bind((host,port))
     print(host)
     server.listen()
     print("listening......")
     con,addr = server.accept()
     print(addr)
     choose='server'
     medium=con
def clien():
     try:
          global con,client,choose,medium
          client = socket.socket()
          host = '127.0.0.1'
          port = 1244
          address = (host,port)
          client.connect(address)
          choose='client'
          medium=client
     except:
          messagebox.showwarning('connection','connection to server failed')
          retry=messagebox.askretrycancel("reconnecting", "want to connect again?")
          if retry== True:
               clien()
          
def connection():
     conchoose=Tk()
     conchoose.geometry("400x150")
     Label(conchoose,text='CHOOSE',font=('arial',30),justify='center').pack()
     ser = Button(conchoose,text="SERVER",font=("Arial",15),command=lambda:[conchoose.destroy(),server()])
     ser.pack()
     ser.place(relx=0.15, rely=0.35, relwidth=0.35, relheight=0.3)
     cli = Button(conchoose,text="CLIENT",font=("Arial",15),command=lambda:[conchoose.destroy(),clien()])
     cli.pack()
     cli.place(relx=0.55, rely=0.35, relwidth=0.35, relheight=0.3)

def chatting():
     chat=Tk()
     chat.geometry('300x450')
     INPUT= Text(chat, height = 10,width = 25,bg = "light yellow")
     if choose=='server':
          
          global con,client
          while True:
               out=input('enter :')
               con.send(f'{out}'.encode())
               p=con.recv(1024).decode()
               print(p)
     if choose=='client':
          while True:
               p=client.recv(1024).decode()
               print(p)  
               out=input('enter :')
               client.send(f'{out}'.encode())
def filetransfer(a):
     a,filename=None,None
     z=messagebox.askquestion("text sharing", "text sharing")
     def browseFiles():
          global filename
          filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (('text files','*.txt'),("all files","*.*")))

     
     if z=='yes':
          file=Tk()
          file.geometry('200x200')
          Button(file,text='choose file',command=lambda:[browseFiles(),file.destroy()]).pack()
          print()
          file.mainloop()
          send=open(filename,'r')
          intext=send.read()
          a.send(f'{intext}'.encode())
     if z=='no':
          #try:
          send=open('C:\\Users\\LENOVO\\Desktop\\file.txt','w')
          intext=a.recv(1024).decode()
          print(intext)
          send.writelines(intext)
          send.close()
          #except:
               #messagebox.showinfo('sharing','not yet connected')

mainwin=Tk()
mainwin.geometry('1000x600')
mainwin.resizable(False,False)
head=Frame(mainwin,bg='grey',height=120,width=1000)
head.pack()
head.place(relx=0, rely=0)
b = Label(head,  bd=5, relief='sunken',text='online connector',font='Aerial',foreground='blue')
b.pack(side=TOP)
b.place(relx=0.35,rely=0.1, relheight=0.5,relwidth=0.3)

contact=Frame(mainwin,bg='blue',height=850,width=250)
contact.pack()
contact.place(rely=0.2,relx=0)
c=Listbox(contact,yscrollcommand=True)
c.pack()
c.place(relwidth=1,relheight=1)

content=Frame(mainwin,bg='orange',height=480,width=750)
content.pack()
content.place(relx=0.25,rely=0.2)
'''separator = ttk.Separator(mainwin, orient='horizontal')
separator.place(relx=0, rely=0.2, relwidth=1, relheight=0)

separator = ttk.Separator(mainwin, orient='vertical')
separator.place(relx=0.25, rely=0.151, relwidth=0.2, relheight=1)'''


ch=Button(content,text='CONNECT',command=connection)
ch.pack()
ch.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.05)
c = Button(mainwin, bg='grey', bd=5,text='CHATTING',font='Aerial',foreground='blue',command=None)
c.pack()
c.place(relx=0.5, rely=0.5, relheight=0.05,relwidth=0.15)
p = Button(mainwin, bg='grey', bd=5,text='IMAGE',font='Aerial',foreground='blue',command=None)
p.pack()
p.place(relx=0.65, rely=0.5, relheight=0.05,relwidth=0.15)
f =Button(mainwin, bg='grey', bd=5,text='FILE',font='Aerial',foreground='blue',command=lambda:[filetransfer(medium)])
f.pack()
f.place(relx=0.5, rely=0.55, relheight=0.05,relwidth=0.15)
v =Button(mainwin, bg='grey', bd=5,text='VIDEO',font='Aerial',foreground='blue',command=None)
v.pack()
v.place(relx=0.65, rely=0.55, relheight=0.05,relwidth=0.15)


mainwin.mainloop()




     


          
               
