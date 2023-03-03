from math import atan
class complex:
  def __init__(self,real,imag):
    self.real = real
    self.imag = imag
  def mod(self):
    return (self.real**2+self.imag**2)**0.5
  def arg(self):
    return atan(self.imag/self.real)
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
