#kalkulator

from Tkinter import *
class LabelDemo(Frame):
    a=0
    b=0
    w=""
    d=0
    def __init__(self):

        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Przyklad")

        self.b1=Button(self,text="1",command=lambda x=1: self.bu(x),width=2,height=1)
        self.b2=Button(self,text="2",command=lambda x=2: self.bu(x),width=2,height=1)
        self.b3=Button(self,text="3",command=lambda x=3: self.bu(x),width=2,height=1)
        self.b4=Button(self,text="4",command=lambda x=4: self.bu(x),width=2,height=1)
        self.b5=Button(self,text="5",command=lambda x=5: self.bu(x),width=2,height=1)
        self.b6=Button(self,text="6",command=lambda x=6: self.bu(x),width=2,height=1)
        self.b7=Button(self,text="7",command=lambda x=7: self.bu(x),width=2,height=1)
        self.b8=Button(self,text="8",command=lambda x=8: self.bu(x),width=2,height=1)
        self.b9=Button(self,text="9",command=lambda x=9: self.bu(x),width=2,height=1)
        self.b0=Button(self,text="0",command=lambda x=0: self.bu(x),width=2,height=1)

        self.bp=Button(self,text="+",command=self.bp,width=2,height=1)
        self.bm=Button(self,text="-",command=self.bm,width=2,height=1)
        self.br=Button(self,text="*",command=self.br,width=2,height=1)
        self.bd=Button(self,text="/",command=self.bd,width=2,height=1)
        self.bw=Button(self,text="=",command=self.bw,width=2,height=1)
        self.bc=Button(self,text="C",command=self.bc,width=2,height=1)

        self.Label1=Label(self,text="KALKULATOR")

        self.Label1.pack(side=TOP)
        self.b1.pack(side=LEFT)
        self.b2.pack(side=LEFT)
        self.b3.pack(side=LEFT)
        self.b4.pack(side=LEFT)
        self.b5.pack(side=LEFT)
        self.b6.pack(side=LEFT)
        self.b7.pack(side=LEFT)
        self.b8.pack(side=LEFT)
        self.b9.pack(side=LEFT)
        self.b0.pack(side=LEFT)
        self.bp.pack(side=RIGHT)
        self.bm.pack(side=RIGHT)
        self.br.pack(side=RIGHT)
        self.bd.pack(side=RIGHT)
        self.bw.pack(side=RIGHT)
        self.bc.pack(side=RIGHT)

    def bu(self,x):
        self.w+=str(x)
        self.a*=10
        self.a+=x
        self.Label1.config(text=self.w)
        print self.a,self.b,self.w

    def bp(self):
        if self.b==0:
            self.b=self.a
            self.a=0
            self.d=1
            self.w+=" + "
            self.Label1.config(text=self.w)
            print self.a,self.b,self.w
        else:
            if self.d==1:
                self.a=self.b+self.a
            if self.d==2:
                self.a=self.b-self.a
            if self.d==3:
                self.a=self.b*self.a
            if self.d==4:
                self.a=self.b/self.a

            self.b=self.a
            self.a=0
            self.d=1
            self.w+=" + "
            self.Label1.config(text=self.w)
            print self.a,self.b,self.w


    def bm(self):
        if self.b==0:
            self.b=self.a
            self.a=0
            self.d=2
            self.w+=" - "
            self.Label1.config(text=self.w)
            print self.a,self.b,self.w
        else:
            if self.d==1:
                self.a=self.b+self.a
            if self.d==2:
                self.a=self.b-self.a
            if self.d==3:
                self.a=self.b*self.a
            if self.d==4:
                self.a=self.b/self.a

            self.b=self.a
            self.a=0
            self.d=2
            self.w+=" - "
            self.Label1.config(text=self.w)
            print self.a,self.b,self.w

    def br(self):
        if self.b==0:
            self.b=self.a
            self.a=0
            self.d=3
            self.w+=" * "
            self.Label1.config(text=self.w)
            print self.a,self.b,self.w
        else:
            if self.d==1:
                self.a=self.b+self.a
            if self.d==2:
                self.a=self.b-self.a
            if self.d==3:
                self.a=self.b*self.a
            if self.d==4:
                self.a=self.b/self.a

            self.b=self.a
            self.a=0
            self.d=3
            self.w+=" * "
            self.Label1.config(text=self.w)
            print self.a,self.b,self.w
    def bd(self):
        if self.b==0:
            self.b=self.a
            self.a=0
            self.d=4
            self.w+=" / "
            self.Label1.config(text=self.w)
            print self.a,self.b,self.w
        else:
            if self.d==1:
                self.a=self.b+self.a
            if self.d==2:
                self.a=self.b-self.a
            if self.d==3:
                self.a=self.b*self.a
            if self.d==4:
                self.a=self.b/self.a

            self.b=self.a
            self.a=0
            self.d=4
            self.w+=" / "
            self.Label1.config(text=self.w)
            print self.a,self.b,self.w

    def bw(self):
        if self.d==1:
            self.a=self.b+self.a
        if self.d==2:
            self.a=self.b-self.a
        if self.d==3:
            self.a=self.b*self.a
        if self.d==4:
            self.a=self.b/self.a
        self.w=str(self.a)
        self.Label1.config(text=self.w)
        self.b=0
        print self.a,self.b,self.w

    def bc(self):
        self.w=0
        self.a=0
        self.b=0
        self.d=0
        self.Label1.config(text=self.w)
        print self.a,self.b,self.w

def main():
    LabelDemo().mainloop()
if __name__=="__main__":
    main()