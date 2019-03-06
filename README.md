# priorityQ
priority queue in python (just for educational purposes...)

### don't really use this...

I wrote this just to learn/understand the bubbleUp and bubbleDown
methods. You don't want to use this class in anything serious. Take a
look at `import heapq` if you need a priority queue in python.

### methods available/usage

    dequeue(self)
        remove and return the highest-priority item 
    enqueue(self, item, priority)
        add an item to the priority queue (position based on priority)
    peek(self)
        return item of root node
    peekPriority(self)
        return priority of root node

    pq = PriorityQueue()
    pq.enqueue("A",40)
    pq.enqueue("B",20)
    pq.enqueue("C",90)
    for i in range(len(pq)):
      item = pq.dequeue()
      print(item)

The above should print:

    C
    A
    B

### analysis

Using a python `list` to represent the heap, here's the analysis of the
various priority queue operations:

    enqueue: O(lg n)
    dequeue: O(lg n)
    peek: O(1)
    peekPriority: O(1)
