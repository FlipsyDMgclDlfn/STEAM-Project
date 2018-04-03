from tkinter import *

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
    area += poly.evaluate(x)
  return area*step

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

class ReimenSums:
    def __init__(self):
        

master = Tk()
