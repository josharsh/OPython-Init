class p:
  def __init__(self, x):
    self.x = x
  df display_p:
    print(x)

class a:
  def __init__(self, x):
    self.x = x
  df display_a:
    print(x)
obA = a(2)
obA.display_a()

class b(a):     #example of single level inheritance of a in b
  def __init__(self, x,y):
    a.__init__(self,x)
    self.y = y
  def display_b:
    print(x, y)
obB = b(2,3)
obB.display_b()

class c(b):     #example of muti-level inheritance of a in b and then b in c
  def __init__(self, x, y ,z):
    a.__init__(self, x)
    b.__init__(self, y)
    c.z = z
  def display_c:
    print(x,y,z)
    
obC = c(2,3,4)
obB.display_c()

class d(a, p):    #multiple inheritance example
  def __init__(self, x, y, z):
    a.__init__(self,x)
    p.__init__(self,y)
  def display_d:
    print(x,y,z)
obD = d(2,34)
obD.display_d()
