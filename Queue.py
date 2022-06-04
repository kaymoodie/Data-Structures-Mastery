class Queue:

    def __init__(self, size):
        self.queue = [None] * size
        self.front = 0
        self.rear = -1
        self.size = size

    def enqueue(self, item):
        if not self.isFull():
            # Change index of rear
            self.rear += 1
            # set first value
            if self.queue[0] is None:
                self.queue[0] = item
            else:
                self.queue[self.rear] = item

    def dequeue(self):
        item = None
        if not self.isEmpty():
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
        if self.rear == self.size - 1:
            self.front = 0
            self.rear = -1
        return item

    def isEmpty(self):
        return self.queue[self.front] is None

    def isFull(self):
        return self.rear == self.size - 1

    def displayQueue(self):

        if not self.isEmpty():
            for item in self.queue:
                print(item)


queue_test = Queue(4)
queue_test.enqueue(1)
queue_test.enqueue(2)
print(queue_test.queue)

queue_test.dequeue()
queue_test.dequeue()
print(queue_test.queue)

data = ["Kanika", "Latoya", "Keanu", "Jazara", "Jammie", "Denyse"]

# Write a Python program to create a queue and display all the members and size of the queue.
names_queue = Queue(len(data))
for item in data:
    names_queue.enqueue(item)

names_queue.displayQueue()
