from tkinter import *
from tkinter import font
from math import *

def evaluateFunc(x,func):
  final = ""
  for i in range(0,len(func)):
    if func[i] == "x":
      final += str(x)
    elif func[i] == "^":
      final += "**"
    else:
      final += func[i]
  return eval(final)
  

def calculateRight(start, end, step, func):
  area = 0
  for x in my_range(start+step, end, step):
    area += evaluateFunc(x,func) * step
  return area
  
def calculateLeft(start, end, step, poly):
  area = 0
  for x in my_range(start, end-step, step):
    area += poly.evaluate(x) * step
  return area

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
        
def getCords(func,start,end,width):
  xs = []
  ys = []
  for i in my_range(start,end+end/width,1*end/width):
    xs += [i]
    ys += [evaluateFunc(i,func)]
    
  xStep = ((max(xs)-min(xs))/width)
  yStep = ((max(ys)-min(ys))/width)
  
  adjust = 0-(min(ys)/yStep)
  
  cords = []
  for i in range(0,len(xs)):
    cords += [[round(xs[i]/xStep),400-round(ys[i]/yStep + adjust)]]
  return cords

def getRectRight(func,start,end,step,width):
  xs = []
  ys = []
  for i in my_range(start,end+end/width,end/width):
    xs += [i]
    ys += [evaluateFunc(i,func)]
    
  yStep = ((max(ys)-min(ys))/width)
  
  adjust = 0-(min(ys)/yStep)
  cords = []
  funcRange = end - start
  xStep = funcRange / width
  rectWidth = step / xStep
  for i in my_range(0,width-rectWidth,rectWidth):
    cords += [([round(xs[round(i)]/xStep),0],[round(xs[round(i+rectWidth)]/xStep),round(ys[round(i+rectWidth)]/yStep+adjust)])]
  return cords

class RiemannSums:
  def __init__(self):
    self.func = "x^2"
    self.width = 400                    ##Width of the graph (also the height)
    self.start = 0                      ##Starting bounds
    self.end = 5                        ##Ending bounds
    self.step = .1                      ##Width of rectangles
    self.C = Canvas(master, bg = "white", height = 600, width = 500)
    self.update()
    S1 = Scale(master,from_=0.01,to=1,command=self.updateSlider,orient=HORIZONTAL,resolution=.01)
    S1.set(.5)
    S1.grid(row=1,columnspan=1)
    S2 = Scale(master,from_=1,to=10,command=self.updateSlider2,orient=HORIZONTAL,resolution=1)
    S2.set(2)
    S2.grid(row=1,column=2,columnspan=1)
    EF = Entry(master,width=12)
    EF.grid(row=3,column=1)
    EF.insert(0,"x^2")
    B = Button(master,text="update",command=lambda:self.updateButton(EF.get()))
    B.grid(row=4,column=1)
    L1 = Label(master,text="Rectangle Width")
    L1.grid(row=3,column = 0)
    L2 = Label(master,text="Max X Value")
    L2.grid(row=3,column=2)
  def updateSlider(self,step):
    self.step = float(step)
    self.update()
  def updateSlider2(self,end):
    self.end = int(end)
    self.update()
  def updateButton(self,func):
    self.func = func
    self.update()
  def update(self):
    self.C.delete(ALL)
    self.xs = []
    self.ys = []
    for i in my_range(self.start,self.end+self.end/self.width,1*self.end/self.width):
      self.xs += [i]
      self.ys += [evaluateFunc(i,self.func)]
    
    self.xStep = ((max(self.xs)-min(self.xs))/self.width)
    self.yStep = ((max(self.ys)-min(self.ys))/self.width)
  
    adjusty = 0-(min(self.ys)/self.yStep)
    
    lines = []
    cords = getCords(self.func,self.start,self.end,self.width)
    for i in range(0,len(cords)-1):
      lines += [self.C.create_line(50+cords[i][0],50+cords[i][1],50+cords[i+1][0],50+cords[i+1][1],fill="red")]
      self.C.grid(row=0,columnspan=16)
    
    rectCords = getRectRight(self.func,self.start,self.end,self.step,self.width)
    for i in range(0,len(rectCords)):
      if adjusty < 0:
        self.C.create_rectangle(50+rectCords[i][0][0],450,50+rectCords[i][1][0],450-rectCords[i][1][1],outline = "blue")        
      elif adjusty >= 400:
        self.C.create_rectangle(50+rectCords[i][0][0],50,50+rectCords[i][1][0],450-rectCords[i][1][1],outline = "blue")
      else:

        self.C.create_rectangle(50+rectCords[i][0][0],450 - adjusty-rectCords[i][0][1],50+rectCords[i][1][0],450-rectCords[i][1][1],outline = "blue")

    self.C.create_text(250,500,text = "y = " + self.func)
    if adjusty >= 0 and adjusty <= 400:
      self.C.create_line(50,450-adjusty,450,450-adjusty)
      self.C.create_text(45,450-adjusty,text="0")
    self.C.create_rectangle(50,50,450,450,outline="green")

    self.C.create_text(250,25,text="Riemann Sums",font=("Courier", 20))
    
    self.C.create_text(25,55,text=str(round(max(self.ys),1)))
    self.C.create_text(25,450,text=str(round(min(self.ys),1)))
    self.C.create_text(50,460,text=str(self.start))
    self.C.create_text(450,460,text=str(self.end))
    
    self.C.create_text(250,550,text=u"\u222B" + " " + self.func + " dx " + u"\u2248" + " " + str(round(calculateRight(self.start,self.end,self.step,self.func),2)))
    self.C.create_text(250,575,text="Aproximated Area")
    ##self.C.create_text(215,540,text=str(self.start),font=("Courier", 8))
    ##self.C.create_text(215,560,text=str(self.end),font=("Courier", 8))
    
    self.C.grid(row=0,columnspan=3)
    

master = Tk()
sums = RiemannSums()
master.mainloop()


  







