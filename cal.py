from tkinter import*

def iCalc(source,side):
    sroreObj = Frame(source,borderwith=4,bd=4,bg="sky blue")
    storeObj.pack(side=side,expand=yes,fill=BOTH)
    return storeObject
def button(source,side,text,command=None):
    storeObj = Button(source,text=text,ommand=command)
    storeObj.pack(side=side,expand=YES,fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('Font','arial 20 bold')
        self.pack(expand=YES,fill=BOTH)
        self.master.title('Calculator')

        display = StringVar()
        Entry(self,relief=RIDGE,
              textvariable=display,justify='right',bd=30,bg="sky blue").pack(side=TOP,expand=YES,fill=BOTH)

        for clearBut in (["CE"],["C"]):
            erase = iCalc(self, TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))

        for NumBut in("789/", "456*", "123-", "0.+"):
            FunctionNum = iCalc(self, TOP)
            for char in NumBut:
                button(FunctionNum, LEFT, char,
                       lambda storeObj=display, q=char: storeObj.set(storeObj.get() + q))
       


if __name__ == '__main__':
    app().mainloop()

    
        
