class p:
  def __init__(self, x):
    self.x = x
  def display_p(self):
    print(self.x)

class a:
  def __init__(self, x):
    self.x = x
  def display_a(self):
    print(self.x)

obA = a(2)
obA.display_a()

class b(a):     #example of single level inheritance of a in b
  def __init__(self, x,y):
    a.__init__(self,x)
    self.y = y
  def display_b(self):
    print(self.x, self.y)
obB = b(2,3)
obB.display_b()

class c(b):     #example of muti-level inheritance of a in b and then b in c
  def __init__(self, x, y ,z):
    a.__init__(self, x)
    b.__init__(self, x, y)
    self.z = z
  def display_c(self):
    print(self.x,self.y,self.z)
    
obC = c(2,3,4)
obC.display_c()

class d(a, p):    #multiple inheritance example
  def __init__(self, x, y, z):
    a.__init__(self,x)
    self.z = z
  def display_d(self):
    print(self.x, self.z)
obD = d(2,34, 5)
obD.display_d()
