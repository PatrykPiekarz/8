#przycisk wyswietlajacy ciag fibonacciego na label

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
        self.hi_there=Button(self,text="FIBONACCI",command=self.say_hi,width=16,height=1)

        #trzy pola etykiet, dwa texty i ikona
        self.Label1=Label(self,text="FIBONACCI")

        #pakujemy wszystko w ramce
        self.hi_there.pack(side=BOTTOM)
        self.Label1.pack(side=LEFT)

    #metoda wywolywana przez quit
    def quit1(self):
        print "Koniec"
        quit()

    #metoda wywolywana przez hej
    def say_hi(self):
        #ciag fibo
        lst = [0,1]
        n = 10
        #print lst[0],"\n",lst[1]
        for i in range (2,n):
            lst.append(lst[i-1]+lst[i-2])
            #print lst[i]
        texts=""
        for i in lst:
            i=str(i)
            texts+= i
            texts+=" "

        self.Label1.config(text=texts)
#program glowny utworz okno labeldemo i osbloz zdarzenia
def main():
    LabelDemo().mainloop()
#jesli nazwa uruchamianego programu to __main__ wywolaj main()
if __name__=="__main__":
    main()