class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_node.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

queue = Queue()
queue.enqueue(100)
queue.enqueue(200)
queue.enqueue(300)
queue.enqueue(300)
queue.enqueue(400)
queue.enqueue(500)
queue.display()  
print("Dequeued:", queue.dequeue())  
queue.display()  
