import unittest, io, sys
from priorityqueue import *
from random import randrange, choice, shuffle
from operator import itemgetter

class TestPriorityQMethods(unittest.TestCase):

  def setUp(self):
    """create priority queues (min and max)"""
    self.maxpq = PriorityQueue("maximum")
    self.minpq = PriorityQueue("minimum")
    self.assertEqual(self.maxpq.getSize(), 0)
    self.assertEqual(self.minpq.getSize(), 0)
    self.items = list("ABCDEFGHIJKLMNOPQ")
    nums = list(range(10,100))  # want unique priorities for some tests
    shuffle(nums)
    self.priorities = []
    self.data = []
    for i in range(len(self.items)):
      pri = nums[i]
      self.priorities.append(pri)
      self.data.append((self.items[i], pri))

  def test_empty(self):
    self.assertEqual(self.maxpq.getSize(), 0)
    self.assertEqual(self.minpq.getSize(), 0)
    self.assertEqual(self.maxpq.isEmpty(), True)
    self.assertEqual(self.minpq.isEmpty(), True)
    self.assertEqual(len(self.maxpq), 0)
    self.assertEqual(len(self.minpq), 0)

  def test_enqueue(self):
    for i in range(len(self.items)):
      item = self.items[i]
      pri = self.priorities[i]
      self.minpq.enqueue(item,pri)
      self.maxpq.enqueue(item,pri)
    self.assertEqual(self.minpq.getSize(), len(self.items))
    self.assertEqual(self.minpq.isEmpty(), False)
    self.assertEqual(self.maxpq.getSize(), len(self.items))
    self.assertEqual(self.maxpq.isEmpty(), False)

  def test_dequeue(self):
    for i in range(len(self.items)):
      item = self.items[i]
      pri = self.priorities[i]
      self.minpq.enqueue(item,pri)
      self.maxpq.enqueue(item,pri)
    self.assertEqual(self.minpq.getSize(), len(self.items))
    self.assertFalse(self.minpq.isEmpty())
    self.assertEqual(self.maxpq.getSize(), len(self.items))
    self.assertFalse(self.maxpq.isEmpty())
    # sort data by priority
    minlist = sorted(self.data, key=itemgetter(1))
    i = 0
    while (not self.minpq.isEmpty()):
      item = self.minpq.dequeue()
      self.assertEqual(item, minlist[i][0])
      i += 1
    self.assertEqual(self.minpq.getSize(), 0)
    self.assertTrue(self.minpq.isEmpty())
    maxlist = sorted(self.data, key=itemgetter(1), reverse=True)
    i = 0
    while (not self.maxpq.isEmpty()):
      item = self.maxpq.dequeue()
      self.assertEqual(item, maxlist[i][0])
      i += 1
    self.assertTrue(self.maxpq.isEmpty())
    self.assertEqual(self.maxpq.getSize(), 0)

  def test_dequeueEmpty(self):
    emptyPQ = PriorityQueue()
    self.assertRaises(Exception, emptyPQ.dequeue)

  def test_badInit(self):
    self.assertRaises(Exception, PriorityQueue, "bad init arg")

  def test_emptyPeeks(self):
    emptyPQ = PriorityQueue()
    self.assertRaises(Exception, emptyPQ.peek)
    self.assertRaises(Exception, emptyPQ.peekItem)
    self.assertRaises(Exception, emptyPQ.peekPriority)

####################################################

if __name__ == '__main__':
  unittest.main()
