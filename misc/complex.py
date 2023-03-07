from math import atan
class complex:
  def __init__(self,real,imag):
    self.real = real
    self.imag = imag
  def mod(self):
    return (self.real**2+self.imag**2)**0.5
  def arg(self):
    return atan(self.imag/self.real)
  def conj(self):
    return complex(self.real,-self.imag)
  def scalardiv(self,k):
    return complex(self.real/k,self.imag/k)
  def __add__(self, other):
    r = self.real + other.real
    i = self.imag + other.imag
    return complex(r,i)
  def __sub__(self, other):
    r = self.real - other.real
    i = self.imag - other.imag
    return complex(r,i)
  def __mul__(self, other):
    a, b = self.real, self.imag
    c, d = other.real, other.imag
    r = a*c - b*d
    i = a*d + b*c
    return complex(r,i)
  def __truediv__(self, other):
    c, d = other.real, other.imag
    k = c**2 + d**2
    x = self * other.conj()
    return x.scalardiv(k)
  def __str__(self):
    if self.imag >= 0:
      return str(self.real) + " + i" + str(self.imag)
    else:
      return str(self.real) + " - i" + str(abs(self.imag))
  def inverse(self):
    return self.conj().scalardiv(self.mod()**2)
