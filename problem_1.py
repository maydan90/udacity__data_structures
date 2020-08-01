class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node  # add data to the next attribute of the tail (i.e. the end of the queue)
            self.tail.next.prev = self.tail  # set the old tail as a previous attribute of the current tail
            self.tail = self.tail.next  # shift the tail (i.e., the back of the queue)
        self.num_elements += 1

    def dequeue(self):
        if self.is_empty():
            return None
        node = self.head  # copy the node reference to a local variable

        self.head = self.head.next  # shift the head (i.e., the front of the queue)
        if self.head:
            self.head.prev = None

        node.prev = None
        node.next = None

        self.num_elements -= 1
        return node

    def move_to_end(self, node):
        if node is self.tail:
            return
        if node is self.head:
            self.enqueue(self.dequeue())
        else:
            node.next.prev = node.prev
            node.prev.next = node.next

            node.prev = None
            node.next = None

            self.enqueue(node)

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def __repr__(self):
        if self.is_empty():
            return 'empty queue'
        node = self.head
        output = ''
        while node:
            output += f'({node.key}, {node.value}) -> '
            node = node.next
        return output


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.order = Queue()
        self._map = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self._map:
            self.order.move_to_end(self._map[key])
            return self._map[key].value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            return

        if key not in self._map:
            new_node = Node(key, value)
            if len(self._map) == self.capacity:
                removed_node = self.order.dequeue()
                del self._map[removed_node.key]
            self.order.enqueue(new_node)
            self._map[key] = new_node


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache1 = LRU_Cache(1)
our_cache1.set(1, 1)
print(our_cache1.get(1))  # returns 1
our_cache1.set(2, 2)
print(our_cache1.get(1))  # returns -1
print(our_cache1.get(2))  # returns 2

our_cache2 = LRU_Cache(128)

for i in range(200):
    our_cache2.set(i, i)
    if i % 100 == 0:
        print(our_cache2.get(5))  # returns 5

print(our_cache2.get(200))  # returns -1
print(our_cache2.get(5))  # returns 5
print(our_cache2.get(11))  # returns -1

# empty cache
our_cache3 = LRU_Cache(0)
our_cache3.set(1, 1)
print(our_cache3.get(1))  # returns -1
print(our_cache3.get(2))  # returns -1
our_cache3.set(2, 2)
print(our_cache3.get(2))  # returns -1
