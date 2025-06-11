class CircularQueue:

    DEFAULT_CAPACITY=10

    def __init__(self):

        self._data = [None] * CircularQueue.DEFAULT_CAPACITY

        self._size = 0

        self._front = 0

    # def __len__(self):
    #     return self._size

    def is_Empty(self):
        return self._size == 0

    def first(self):
        if self.is_Empty():
            raise Empty("Queue is Empty!")
        return self._data[self._front]

    def dequeue(self):
        if self.is_Empty():
            raise Empty("Queue is Empty for Dequeue Operation!")
        front = (self._front+1) % len(self._data)
        dequeued_element = self._data[self._front]

        self._data[self._front] = None #Garbage collection

        self._size -=1

        return dequeued_element

    def enqueue(self,element):
      if self._size == len(self._data):
          #print("Queue is Full") before you add resizing when self._size == len(self._data) then no other value will be added in the queue
          #return
          self._resize(2 * len(self._data))

      tail = (self._front + self._size) % len(self._data)

      self._data[tail] = element

      self._size = self._size + 1


    def _resize(self,new_capacity):
        ...


class Empty(Exception):
  pass

  if __name__=="__main__":

      object_queue= CircularQueue()

      insert_elements= [11,22,33,44,55,66,77,88,99,110,121]

      for element in insert_elements:
          object_queue.enqueue(element)

          print(f"Added Element: {element}")
          print(f"The new size of the Queue:  {object_queue._size}")#len(object_queue)
          print("\n Current Queue Representation:")




