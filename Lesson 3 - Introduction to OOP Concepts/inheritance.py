class p:
  def __init__(self, x):
      """
      Initialize the x

      Args:
          self: (todo): write your description
          x: (int): write your description
      """
    self.x = x
  def display_p(self):
      """
      Display p : x

      Args:
          self: (todo): write your description
      """
    print(self.x)

class a:
  def __init__(self, x):
      """
      Initialize the x

      Args:
          self: (todo): write your description
          x: (int): write your description
      """
    self.x = x
  def display_a(self):
      """
      Display the current screen

      Args:
          self: (todo): write your description
      """
    print(self.x)

obA = a(2)
obA.display_a()

class b(a):     #example of single level inheritance of a in b
  def __init__(self, x,y):
      """
      Initialize a new data.

      Args:
          self: (todo): write your description
          x: (int): write your description
          y: (int): write your description
      """
    a.__init__(self,x)
    self.y = y
  def display_b(self):
      """
      Prints the screen.

      Args:
          self: (todo): write your description
      """
    print(self.x, self.y)
obB = b(2,3)
obB.display_b()

class c(b):     #example of muti-level inheritance of a in b and then b in c
  def __init__(self, x, y ,z):
      """
      Initialize the z - axis

      Args:
          self: (todo): write your description
          x: (int): write your description
          y: (int): write your description
          z: (int): write your description
      """
    a.__init__(self, x)
    b.__init__(self, x, y)
    self.z = z
  def display_c(self):
      """
      Display the cursor position.

      Args:
          self: (todo): write your description
      """
    print(self.x,self.y,self.z)
    
obC = c(2,3,4)
obC.display_c()

class d(a, p):    #multiple inheritance example
  def __init__(self, x, y, z):
      """
      Initialize z - axis

      Args:
          self: (todo): write your description
          x: (int): write your description
          y: (int): write your description
          z: (int): write your description
      """
    a.__init__(self,x)
    self.z = z
  def display_d(self):
      """
      Prints : class

      Args:
          self: (todo): write your description
      """
    print(self.x, self.z)
obD = d(2,34, 5)
obD.display_d()
