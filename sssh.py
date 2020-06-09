import argparse,tkinter
class Slide:
    def __init__(self):
        self.text=[]
        self.posys=[]
        self.posxs=[]
        self.fonts=[]
        self.images=[]
        self.imageposxs=[]
        self.imageposys=[]
        self.canv=tkinter.Canvas(width=10000,height=10000)
        self.canv.pack()
        self.textindex=5
        
    def add_text(self,txt,font='Times 20' ):
        self.text.append(txt)
        self.posys.append(self.textindex*12)
        self.posxs.append(850+len(txt)*(2.825))
        self.fonts.append(font)
        self.textindex+=1
        
    def add_title(self,title,font='CourierNew 30',color='black'):
        self.title=Title(text=title,font=font,color=color)
        self.titargs=self.title.create()
    def add_image(self,posx,posy,image):
        img=tkinter.PhotoImage(file=image)
        self.images.append(img)
        self.imageposxs.append(posx)
        self.imageposys.append(posy)

    def show(self):
        for i in self.text:
            self.canv.create_text(self.posxs[self.text.index(i)],self.posys[self.text.index(i)],text="● "+i,font=self.fonts[self.text.index(i)])
        self.canv.create_text(self.titargs[0],self.titargs[1],text=self.titargs[2],font=self.titargs[3],fill=self.titargs[4])
        for i in self.images:    
            self.canv.create_image(self.imageposxs[self.images.index(i)],self.imageposys[self.images.index(i)],image=i,anchor='nw')
        self.canv.pack()

        tkinter.mainloop()
    def canvas(self):
        return self.canv

class Title:
    def __init__(self,text,posxtit=960,posytit=30,font='Times 30',color='black'):
        self.text=text
        self.posxtit=posxtit
        self.posytit=posytit
        self.font=font
        self.color=color
    def create(self):
        return([self.posxtit,self.posytit,self.text,self.font,self.color])

class SlideShow:
    def __init__(self,*piano):
        self.piano=list(piano)
        self.slideindex=-1
    def nex(self,foo):
        self.slideindex+=1
        self.piano[self.slideindex].show()
            
    def play(self):
        for i in self.piano:
            i.canvas().bind('<Button-1>',self.nex)
        self.piano[0].show()

