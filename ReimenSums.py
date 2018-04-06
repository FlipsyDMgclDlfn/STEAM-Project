from tkinter import *
from tkinter import font
class Polynomial(object):
  
  ##the code runs this automatically when initializing a polynomial
  def __init__(self, coefficients):
    self.coeff = coefficients
    
  ##returns the value of the polynomial given the value of 'x'  
  def evaluate(self, x):
    a = 0
    for i in range(0, max(self.coeff) + 1):
      if i in self.coeff:
        a += self.coeff[i] * x**i
    return a
    
  ##returns a string that is a writen representation of the polynomial  
  def __str__(self):
    strTerms = ''
    if 0 in self.coeff:
      terms = [str(self.coeff[0])]
    else:
      terms = [str(0)]
    for j in range(1,max(self.coeff)+1):
      if j in self.coeff:
        if self.coeff[j] != 0:
          if abs(self.coeff[j]) == 1:
            if self.coeff[j] > 0:
              if j == 1:
                terms += [' + x']
              else:  
                terms += [' + x^' + str(j)]
            else:
              if j == 1:
                terms += [' - x']
              else:
                terms += [' - x^' + str(j)]
          else:
            if self.coeff[j] > 0:
              if j == 1:
                terms += [' + ' + str(self.coeff[j]) + 'x']
              else:
                terms += [' + ' + str(self.coeff[j]) + 'x^' + str(j)]
            else:
              if j == 1:
                terms += [' - ' + str(abs(self.coeff[j])) + 'x']
              else:
                terms += [' - ' + str(abs(self.coeff[j])) + 'x^' + str(j)]
    for k in range(0,len(terms)):
      strTerms += terms[k]
    return strTerms
    
  ##returns the power of the polynomial  
  def __len__(self):
    return max(self.coeff)







def calculateRight(start, end, step, poly):
  area = 0
  for x in my_range(start+step, end, step):
    area += poly.evaluate(x) * step
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
        
def getCords(poly,start,end,width):
  xs = []
  ys = []
  for i in my_range(start,end+end/width,1*end/width):
    xs += [i]
    ys += [poly.evaluate(i)]
    
  xStep = ((max(xs)-min(xs))/width)
  yStep = ((max(ys)-min(ys))/width)
  
  adjust = 0-(min(ys)/yStep)
  
  cords = []
  for i in range(0,len(xs)):
    cords += [[round(xs[i]/xStep),400-round(ys[i]/yStep + adjust)]]
  return cords

def getRectRight(poly,start,end,step,width):
  xs = []
  ys = []
  for i in my_range(start,end+end/width,end/width):
    xs += [i]
    ys += [poly.evaluate(i)]
    
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
    self.poly = Polynomial({0:0,2:1})   ##Polynomial working with
    self.width = 400                    ##Width of the graph (also the height)
    self.start = 0                      ##Starting bounds
    self.end = 5                        ##Ending bounds
    self.step = .1                      ##Width of rectangles
    self.C = Canvas(master, bg = "white", height = 600, width = 500)
    self.update()
    S1 = Scale(master,from_=0.01,to=1,command=self.updateSlider,orient=HORIZONTAL,resolution=.01)
    S1.set(.5)
    S1.grid(row=1,columnspan=8)
    S2 = Scale(master,from_=1,to=10,command=self.updateSlider2,orient=HORIZONTAL,resolution=1)
    S2.set(2)
    S2.grid(row=1,column=8,columnspan=8)
    LA = Label(master,text="a")
    LA.grid(row=2,column=2)
    LB = Label(master,text="bx")
    LB.grid(row=2,column=4)
    LC = Label(master,text="cx^2")
    LC.grid(row=2,column=6)
    LD = Label(master,text="dx^3")
    LD.grid(row=2,column=8)
    LE = Label(master,text="ex^4")
    LE.grid(row=2,column=10)
    LF = Label(master,text="fx^5")
    LF.grid(row=2,column=12)
    L1 = Label(master,text="+")
    L1.grid(row=2,column=3)
    L2 = Label(master,text="+")
    L2.grid(row=2,column=5)
    L3 = Label(master,text="+")
    L3.grid(row=2,column=7)
    L4 = Label(master,text="+")
    L4.grid(row=2,column=9)
    L5 = Label(master,text="+")
    L5.grid(row=2,column=11)
    EA = Entry(master,width=3)
    EA.grid(row=3,column=2)
    EA.insert(0,0)
    EB = Entry(master,width=3)
    EB.grid(row=3,column=4)
    EB.insert(0,0)
    EC = Entry(master,width=3)
    EC.grid(row=3,column=6)
    EC.insert(0,1)
    ED = Entry(master,width=3)
    ED.grid(row=3,column=8)
    ED.insert(0,0)
    EE = Entry(master,width=3)
    EE.grid(row=3,column=10)
    EE.insert(0,0)
    EF = Entry(master,width=3)
    EF.grid(row=3,column=12)
    EF.insert(0,0)
    B = Button(master,text="update",command=lambda:self.updateButton(EA.get(),EB.get(),EC.get(),ED.get(),EE.get(),EF.get()))
    B.grid(row=4,column=7)
  def updateSlider(self,step):
    self.step = float(step)
    self.update()
  def updateSlider2(self,end):
    self.end = int(end)
    self.update()
  def updateButton(self,a,b,c,d,e,f):
    self.poly= Polynomial({0:int(a),1:int(b),2:int(c),3:int(d),4:int(e),5:int(f)})
    self.update()
  def update(self):
    self.C.delete(ALL)
    self.xs = []
    self.ys = []
    for i in my_range(self.start,self.end+self.end/self.width,1*self.end/self.width):
      self.xs += [i]
      self.ys += [self.poly.evaluate(i)]
    
    self.xStep = ((max(self.xs)-min(self.xs))/self.width)
    self.yStep = ((max(self.ys)-min(self.ys))/self.width)
  
    adjusty = 0-(min(self.ys)/self.yStep)
    
    lines = []
    cords = getCords(self.poly,self.start,self.end,self.width)
    for i in range(0,len(cords)-1):
      lines += [self.C.create_line(50+cords[i][0],50+cords[i][1],50+cords[i+1][0],50+cords[i+1][1],fill="red")]
      self.C.grid(row=0,columnspan=16)
    
    rectCords = getRectRight(self.poly,self.start,self.end,self.step,self.width)
    for i in range(0,len(rectCords)):
      self.C.create_rectangle(50+rectCords[i][0][0],450 - adjusty-rectCords[i][0][1],50+rectCords[i][1][0],450-rectCords[i][1][1],outline = "blue")

    self.C.create_text(250,500,text = "y = " + self.poly.__str__())
    self.C.create_line(50,450-adjusty,450,450-adjusty)
    self.C.create_rectangle(50,50,450,450,outline="green")
    
    self.C.create_text(25,55,text=str(round(max(self.ys),1)))
    self.C.create_text(25,450,text=str(round(min(self.ys),1)))
    self.C.create_text(50,460,text=str(self.start))
    self.C.create_text(450,460,text=str(self.end))
    self.C.create_text(45,450-adjusty,text="0")
    self.C.create_text(250,550,text=u"\u222B" + " " + self.poly.__str__() + " dx " + u"\u2248" + " " + str(round(calculateRight(self.start,self.end,self.step,self.poly),2)))
    ##self.C.create_text(215,540,text=str(self.start),font=("Courier", 8))
    ##self.C.create_text(215,560,text=str(self.end),font=("Courier", 8))
    
    self.C.grid(row=0,columnspan=16)
    

master = Tk()
sums = RiemannSums()
master.mainloop()


  







