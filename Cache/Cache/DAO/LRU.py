from DAO.EvictionPolicy import EvictionPolicy


class Node:
    def __init__(self, key, val):
        self.k = key
        self.v = val
        self.next = None
        self.prev = None

class LRU(EvictionPolicy):

    def __init__(self, capacity, map):
        self.cap = capacity
        self.totalNodes = 0
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.store = map

    def updatePosition(self, node):
        rightPrev = self.right.prev
        rightPrev.next = node
        node.prev = rightPrev
        node.next = self.right
        self.right.prev = node

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key):
        if key not in self.store:
            return -1
        node = self.store[key]
        self.removeNode(node)
        self.updatePosition(node)
        return node.v

    def put(self, key, value):
        if key in self.store:
            node = self.store[key]
            node.v = value
            self.removeNode(node)
            self.updatePosition(node)
        else:
            if self.totalNodes == self.cap:
                nodeToRemove = self.left.next
                self.removeNode(nodeToRemove)
                del self.store[nodeToRemove.k]
            else:
                self.totalNodes += 1
            newNode = Node(key,value)
            self.store[key] = newNode
            self.updatePosition(newNode)

    def remove(self, key):
        if key in self.store:
            self.removeNode(self.store[key])
            del self.store[key]
            return True
        else:
            return False