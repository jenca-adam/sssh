import argparse,tkinter
class Slide:
    def __init__(self):
        self.text=[]
        self.posys=[]
        self.posxs=[]
        self.fonts=[]
        self.canv=tkinter.Canvas()
        self.canv.pack()
        self.textindex=5
        
    def add_text(self,txt,font='Times 20' ):
        self.text.append(txt)
        self.posys.append(self.textindex*12)
        self.posxs.append(50+len(txt)*(2.825))
        self.fonts.append(font)
        self.textindex+=1
        
    def add_title(self,title,font='CourierNew 30',color='black'):
        self.title=Title(text=title,font=font,color=color)
        self.titargs=self.title.create()
    def show(self):
        for i in self.text:
            self.canv.create_text(self.posxs[self.text.index(i)],self.posys[self.text.index(i)],text="● "+i,font=self.fonts[self.text.index(i)])
        self.canv.create_text(self.titargs[0],self.titargs[1],text=self.titargs[2],font=self.titargs[3],fill=self.titargs[4])
        self.canv.pack()

        tkinter.mainloop()
class Title:
    def __init__(self,text,posxtit=185,posytit=30,font='Times 20',color='black'):
        self.text=text
        self.posxtit=posxtit
        self.posytit=posytit
        self.font=font
        self.color=color
    def create(self):
        return([self.posxtit,self.posytit,self.text,self.font,self.color])

    
