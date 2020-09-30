class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
            
    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self._remove(self.table[key])
        node = Node(key, value)
        self.table[key] = node
        self._add(node)
        if len(self.table) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.table[node.key]
            
        
    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def _add(self,  node: Node) -> None:
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
