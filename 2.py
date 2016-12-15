from Tkinter import *
class LabelDemo(Frame):
    def __init__(self):
        #tworzy trzy etykiety i dwa przyciski i je pakuje
        #tworzy obiekt ramka w ktorym umieszczamy widgety
        #ramka jest upakowana w glownym oknie i ma tytul
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Przyklad")

        #dwa przyciski:quit i hej. klikniecie wywola quit1 i say_hi
        self.button=Button(self,text="QUIT",fg="red",
                           command=self.quit1,width=16,height=1)
        self.hi_there=Button(self,text="YEAH",command=self.say_hi,width=16,height=1)

        #trzy pola etykiet, dwa texty i ikona
        self.Label1=Label(self,text="Etykieta tekstowa")
        self.Label2=Label(self,text="Etykieta tekstowa z ikona")
        self.Label3=Label(self,bitmap="warning")

        #pakujemy wszystko w ramce
        self.button.pack(side=BOTTOM)
        self.hi_there.pack(side=BOTTOM)
        self.Label1.pack(side=LEFT)
        self.Label2.pack(side=LEFT)
        self.Label3.pack(side=LEFT)

    #metoda wywolywana przez quit
    def quit1(self):
        print "Koniec"
        quit()

    #metoda wywolywana przez hej
    def say_hi(self):
        print "YEAH"
#program glowny utworz okno labeldemo i osbloz zdarzenia
def main():
    LabelDemo().mainloop()
#jesli nazwa uruchamianego programu to __main__ wywolaj main()
if __name__=="__main__":
    main()