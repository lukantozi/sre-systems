class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int): #-> int:
        return self.table[key] if key in self.table else -1


    def add_node(self, node):
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        self.tail.prev = tmp
        tmp.prev = node

    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = None
        node.prev = None

        
    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table[key] = value
            node = Node(key, value)
            self.add_node(node)
            self.remove_node(self.tail.prev)
        else:
            node = Node(key, value)
            self.add_node(node)
            self.table[key] = value
        if len(self.table) > self.capacity:
            self.remove_node(self.tail.prev)
            self.table.pop(self.tail.prev.value)





lRUCache = LRUCache(2)
print()
lRUCache.put(1, 1) 
print(f"table after put(1,1): {lRUCache.table}")
head = lRUCache.head
print("Linked list below:")
while head:
    print(head.value, end=" ")
    head = head.next
print()
print()

lRUCache.put(2, 2) 
print(f"table after (2,2): {lRUCache.table}")

print("Linked list below:")
head = lRUCache.head
while head:
    print(head.value, end=" ")
    head = head.next
print()
print()

print(f"get(1): {lRUCache.get(1)}")

print()
lRUCache.put(3, 3) # {1 <-> 3}
print(f"table after put(3,3): {lRUCache.table}")
print("Linked list below:")
head = lRUCache.head
while head:
    print(head.value, end=" ")
    head = head.next

print()
print()
print(f"get(2): {lRUCache.get(2)}")


lRUCache.put(4,4)
print(f"table after put(4,4): {lRUCache.table}")
print("Linked list below:")
head = lRUCache.head
while head:
    print(head.value, end=" ")
    head = head.next
print()
print(f"table: {lRUCache.table}")

