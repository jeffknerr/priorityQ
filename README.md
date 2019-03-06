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
