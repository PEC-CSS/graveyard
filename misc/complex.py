from math import atan
class complex:
  def __init__(self,real,imag):
    self.real = real
    self.imag = imag
  def mod(self):
    return (self.real**2+self.imag**2)**0.5
  def arg(self):
    return atan(self.imag/self.real)
