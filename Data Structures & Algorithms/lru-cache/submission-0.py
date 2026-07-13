class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.numel = 0
        self.mapping = {}  # key to node
        self.head = Node(key=None, val=None)  # dummy left (lru)
        self.tail = Node(key=None, val=None)  # dummy right (mru)
        self.head.right, self.tail.left = self.tail, self.head

    def remove(self, node):
        node.left.right = node.right
        node.right.left = node.left
    
    def insert_at_tail(self, node):
        prev = self.tail.left
        prev.right = node
        node.left = prev
        node.right = self.tail
        self.tail.left = node

    def get(self, key: int) -> int:
        if key in self.mapping:
            # move to end of list
            node = self.mapping[key]
            self.remove(node)
            self.insert_at_tail(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            # move to end of list
            node = self.mapping[key]
            self.remove(node)
            self.insert_at_tail(node)
            node.val = value
        else:
            new_node = Node(key=key, val=value)
            self.insert_at_tail(new_node)
            self.numel += 1
            self.mapping[key] = new_node
        
        if self.numel > self.capacity:
            victim = self.head.right
            del self.mapping[victim.key]
            self.remove(victim)
            self.numel -= 1





