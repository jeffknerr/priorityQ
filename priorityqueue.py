"""
Priority Queue Class

J. Knerr
Dec 2018
"""

from pqnode import *

class PriorityQueue(object):

  def __init__(self, qtype="maximum"):
    """priority queue constructor: creates max PQ by default"""
    self.arr = []
    qt = qtype.lower()
    if (qt == "maximum" or qt == "minimum"):
      self.qtype = qt
    else:
      raise Exception("Priority Queue must be minimum or maximum.")

  def __repr__(self):
    return "%s(%s)" % (self.__class__.__name__, self.qtype)
  def __str__(self):
    s = "PQSize: %d" % len(self.arr)
    if len(self.arr) > 0:
      s += ", Root: %s" % (self.arr[0])
    return s

  def getSize(self):    
    """return size of priority queue"""
    return len(self.arr)
  def __len__(self):
    """return size of priority queue"""
    return len(self.arr)
  def isEmpty(self):  
    """return True if priority queue is empty, False if not"""
    return len(self.arr) == 0

# ---------------------------------------------- #

def main():
  """some basic test code"""

  # make PQ
  pq = PriorityQueue()
  print(pq)
  assert(pq.getSize()==0)
  assert(pq.isEmpty()==True)
  assert(len(pq)==0)
  minpq = PriorityQueue("minimum")
  print(minpq)
  # bad = PriorityQueue("bad") 

if __name__ == "__main__":
  main()
