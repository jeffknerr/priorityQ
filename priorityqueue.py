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

  def peek(self):  
    """return item of root node, or throw exception"""
    if len(self.arr) > 0:
      return self.arr[0].getItem()
    else:
      raise Exception("peek called on empty Priority Queue...")
  def peekItem(self):  
    """return item of root node, or throw exception"""
    return self.peek()
  def peekPriority(self):  
    """return priority of root node, or throw exception"""
    if len(self.arr) > 0:
      return self.arr[0].getPriority()
    else:
      raise Exception("peekPriority called on empty Priority Queue...")

  def enqueue(self, item, priority):
    """add an item to the priority queue (position based on priority)"""
    n = PQNode(item, priority)
    self.arr.append(n)
    newindex = len(self.arr) - 1
    self._bubbleUp(newindex)

  def _bubbleUp(self, index):
    """given index, check if node should be swapped up"""
    if index != 0:
      parentIndex = (index - 1)//2
      if self._mycmp(self.arr[index].getPriority(), self.arr[parentIndex].getPriority()):
        # swap them, call again
        self.arr[index], self.arr[parentIndex] = self.arr[parentIndex], self.arr[index]
        self._bubbleUp(parentIndex)

  def dequeue(self):
    """remove and return the highest-priority item (unless q is empty)"""
    if len(self.arr) <= 0:
      raise Exception("dequeue called on empty Priority Queue...")
    save = self.arr[0].getItem()
    if len(self.arr) > 1:
      # move last to root
      lastindex = len(self.arr) - 1
      self.arr[0] = self.arr[lastindex]
      # remove last item
      self.arr.pop()
      # now bubble down the new root item
      self._bubbleDown(0)
    return save

  def _bubbleDown(self, index):
    """given index, check if node should be swapped down"""
    lci = 2*index + 1   # left child index
    rci = 2*index + 2   # right child index
    length = len(self.arr)
    if (lci < length) and (rci < length):
      # we have two children to compare
      if self._mycmp(self.arr[lci].getPriority(), self.arr[rci].getPriority()):
        cmpindex = lci
      else:
        cmpindex = rci
    elif lci < length:
      # just a left child
      cmpindex = lci
    elif rci < length:
      # can't have just a right child in a complete tree!!!?!?!?
      raise Exception("something is wrong with this Priority Queue...")
    else:
      # no children, so nothing to do
      return

    # if we get here...see if we should swap and keep going
    if self._mycmp(self.arr[cmpindex].getPriority(), self.arr[index].getPriority()):
      # swap them, call again
      self.arr[cmpindex], self.arr[index] = self.arr[index], self.arr[cmpindex]
      self._bubbleDown(cmpindex)

  def _mycmp(self, A, B):
    """compare two items, based on min/max priority queue"""
    if self.qtype == "maximum":
      return A >= B
    else:
      return A <= B

  def pl(self):
    """print the list -- for debugging help...."""
    print(self.arr)

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
  items = list("ABCDEFG")
  priors = [5,20,8,3,50,4,10]
  for i in range(len(items)):
    pq.enqueue(items[i], priors[i])
  assert(len(pq)==len(items))
  assert(pq.getSize()==len(items))
  assert(pq.isEmpty()==False)
  assert(pq.peek()=="E")
  assert(pq.peekItem()=="E")
  assert(pq.peekPriority()==50)
  print(pq)
  pq.pl()
  for i in range(len(items)):
    minpq.enqueue(items[i], priors[i])
  assert(len(minpq)==len(items))
  assert(minpq.getSize()==len(items))
  assert(minpq.isEmpty()==False)
  assert(minpq.peek()=="D")
  assert(minpq.peekItem()=="D")
  assert(minpq.peekPriority()==3)
  print(minpq)
  minpq.pl()
  for i in range(len(minpq) + 1):
    print(minpq.peekItem(), minpq.peekPriority())
    # dequeue root item....
    item = minpq.dequeue()
    print("dequeued root: ", item)

if __name__ == "__main__":
  main()
