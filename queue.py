import sys
class Queue:
    def __init__(self, size):
        self.myQueue = []
        self.queueSize = size
    def isFull(self):
        if len(self.myQueue) == self.queueSize:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if not self.isFull():
            self.myQueue.append(value)
            print("Element enqueued: ", value)
        else:
            print("Queue is full. Cannot enqueue.")    
        
size = int(input("Enter the size of the queue: "))
queue = Queue(size)
print("Queue created with size: ", queue.queueSize)
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print ("4. Delete Queue ")
    print("5. peek")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if len(queue.myQueue) < queue.queueSize:
            element = int(input("Enter the element to enqueue: "))
            queue.myQueue.append(element)
            print("Element enqueued: ", element)
        else:
            print("Queue is full. Cannot enqueue.")
    elif choice == 2:
        if len(queue.myQueue) > 0:
            element = queue.myQueue.pop(0)
            print("Element dequeued: ", element)
        else:
            print("Queue is empty. Cannot dequeue.")
    elif choice == 3:
        print("Current Queue: ", queue.myQueue)
    elif choice == 4:
        queue.myQueue.clear()
        print("Queue deleted.")
    elif choice == 5:
        if len(queue.myQueue) > 0:
            print("Front element: ", queue.myQueue[0])
        else:
            print("Queue is empty.")
    elif choice == 6:
        print("Exiting...")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")