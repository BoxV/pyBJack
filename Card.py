class Cards:
  names = {1: "A", 11: "J", 12: "Q", 13: "K"}

  def __init__ (self, value):
    self.value = value
    if (value > 10):
      self.isFace = True
    else:
      self.isFace = False
  
  def getName (self):
    if (self.value in Cards.names):
      return Cards.names[self.value]
    else:
      return str(self.value)

  def getPoints (self):
    if (self.isFace):
      return 10
    elif (self.value == 1):
      return 11
    else:
      return self.value

  def __str__(self):
    return Cards.getName(self)

  def __repr__(self):
    return str(self)