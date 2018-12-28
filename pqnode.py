"""
Priority Queue Node Class

Nodes to be used in PriorityQueue. Each node stores an item
and a priority for that item.

J. Knerr
Dec 2018
"""

class PQNode(object):

  def __init__(self, item, priority):
    """pq node constructor: item to store and priority"""
    self.item = item
    self.priority = priority

  def __repr__(self):
    """goal is to be unambiguous"""
    # https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
    return "%s(%s,%s)" % (self.__class__.__name__, str(self.item), str(self.priority))

  def __str__(self):
    """__str__ method for pqnode class"""
    return "priority: %4s,  item: %10s" % (self.priority, self.item)

  # getters and setters
  def getItem(self):    
    """get item from node"""
    return self.item
  def getPriority(self):
    """get priority from node"""
    return self.priority
  def setItem(self, item):
    """change item stored in node"""
    self.item = item
  def setPriority(self, priority):
    """change priority of node"""
    self.priority = priority

# ---------------------------------------------- #

def main():
  """simple tests"""

  n1 = PQNode("A", 356)
  print(n1)
  assert(n1.getItem()=="A")
  assert(n1.getPriority()==356)
  n2 = PQNode("hello", "M")
  print(n2)
  assert(n2.getItem()=="hello")
  assert(n2.getPriority()=="M")
  n3 = PQNode(3.14159, 21)
  print(n3)
  assert(n3.getItem()==3.14159)
  assert(n3.getPriority()==21)

if __name__ == "__main__":
  main()
