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
  for i in my_range(start,end+end/width,end/width):
    xs += [i]
    ys += [poly.evaluate(i)]
    
  xStep = ((max(xs)-min(xs))/width)
  yStep = ((max(ys)-min(ys))/width)
  
  adjust = 0-(min(ys)/yStep)
  
  cords = []
  for i in range(0,len(xs)):
    cords += [[round(xs[i]/xStep),round(ys[i]/yStep + adjust)]]
  return cords

def getRectLeft(poly,start,end,step,width):
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
    cords += [([0,round(ys[round(i)]/yStep+adjust)],[round(xs[round(i+rectWidth)]/xStep),round(ys[round(i+rectWidth)]/yStep+adjust)])]
  return cords
  
poly = Polynomial({0:-1,2:1}) ##Polynomial working with
width = 400                   ##Width of the graph (also the height)
start = 0                     ##Starting bounds
end = 2                       ##Ending bounds
step = .5                     ##Width of rectangles
print(getRectLeft(poly,start,end,step,width)) 


  







