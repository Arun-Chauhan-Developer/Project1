from tkinter import *
from tkinter import messagebox
class MyWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self.config(bg="powder blue")
        self.geometry("700x700+500+100")
        self.wincob=[{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
        self.s1=set()
        self.s2=set()
        self.turn=True
        self.count=0
        self.st=DISABLED
        self.p1='Player Red'
        self.p2='Player Green'
        self.DrawButton()
        self.Expand()

    def DrawButton(self):
        self.lb=[]
        for i in range(3):
            for j in range(3):
                self.lb.append(Button(self,command=lambda t=(i,j):self.Display(t),state=self.st))
                self.lb[-1].grid(row=i,column=j,padx=10,pady=10,sticky='nswe')
        self.pl1=Label(self,bg='red',fg='blue',bd=5,relief=RAISED,font='arial 10 bold')
        self.pl1.grid(row=3,column=0,padx=10,pady=10,ipadx=10,ipady=10,sticky='nswe')
        self.start=Button(self,text='Start',command=self.Statebutton,bg='yellow',fg='blue',bd=5,relief=RAISED,font='arial 14 bold')
        self.start.grid(row=3,column=1,padx=10,pady=10,ipadx=10,ipady=10,sticky='nswe')
        self.pl2=Label(self,bg='green',fg='blue',bd=5,relief=RAISED,font='arial 10 bold')
        self.pl2.grid(row=3,column=2,padx=10,pady=10,ipadx=10,ipady=10,sticky='nswe')

    def Expand(self):
        for i in range(4):
            self.grid_rowconfigure(i,weight=1)
        for j in range(3):
            self.grid_columnconfigure(j,weight=1)

    def Statebutton(self):
        self.st=ACTIVE
        self.DrawButton()

    def Display(self,t):
        i=t[0]*3+t[1]
        if self.turn:
            self.lb[i]['bg']='red'
            self.pl1['text']='Player 1'
            self.pl2['text']=''
            self.s1.add(i)
            self.turn=False
        else:
            self.lb[i]['bg']='green'
            self.pl1['text']=''
            self.pl2['text']='Player 2'
            self.s2.add(i)
            self.turn=True
        self.count=self.count+1
        if self.count>=5:
            self.Result()
        if self.count==9:
            messagebox.showinfo("Result","Game Draw")
            self.ReSet()

    def Result(self):
        for s in self.wincob:
            if s<=self.s1:
                messagebox.showinfo("Result","Player 1 Win")
                self.ReSet()
        for s in self.wincob:
            if s<=self.s2:
                messagebox.showinfo("Result","Player 2 Win")
                self.ReSet()

    def ReSet(self):
        self.s1=set()
        self.s2=set()
        self.st=DISABLED
        self.turn=True
        self.count=0
        self.DrawButton()
        self.Expand()

root=MyWindow()
root.mainloop()
