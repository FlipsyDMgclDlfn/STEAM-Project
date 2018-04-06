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
    self.poly = Polynomial({0:0,3:1,2:-1})   ##Polynomial working with
    self.width = 400                    ##Width of the graph (also the height)
    self.start = 0                      ##Starting bounds
    self.end = 5                        ##Ending bounds
    self.step = .1                      ##Width of rectangles
    self.C = Canvas(master, bg = "white", height = 600, width = 500)
    self.update()
    B = Scale(master,from_=0.01,to=1,command=self.updateSlider,orient=HORIZONTAL,resolution=.01)
    B.set(.5)
    B.pack()
    C = Scale(master,from_=1,to=10,command=self.updateSlider2,orient=HORIZONTAL,resolution=1)
    C.set(2)
    C.pack()
  def updateSlider(self,step):
    self.step = float(step)
    self.update()
  def updateSlider2(self,end):
    self.end = int(end)
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
      self.C.pack()
    
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
    
    self.C.pack()
    

master = Tk()
sums = RiemannSums()
master.mainloop()


  







