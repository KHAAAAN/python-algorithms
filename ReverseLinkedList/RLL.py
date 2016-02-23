class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, data): #inOrder
        cur = self.root
        prev = cur
        
        #root cases
        if self.root is None or data < self.root.data:
            self.root = Node(data)
            if cur is not None:
                self.root.next = cur 
            return
        
        #middle or last cases
        while cur is not None and data > cur.data:
            prev = cur
            cur = cur.next

        #last case
        if cur is None:
            prev.next = Node(data)
            return
        
        #middle case
        prev.next = Node(data)
        prev.next.next = cur
        return

    def __PLL(self, node):
        if node is None:
            return

        print(node.data)
        self.__PLL(node.next)

    def print(self):
        self.__PLL(self.root)

def RVL(cur, prev): #Recursive
    if cur is None:
        return prev

    temp = cur
    cur = cur.next
    temp.next = prev

    prev = temp
    return RVL(cur, prev)

def IRVL(LL): #iterative
    cur = LL.root
    prev = None

    while cur is not None:
        temp = cur
        cur = cur.next
        temp.next = prev
        prev = temp

    LL.root = prev


def RevLinkedList(LL):
    LL.root = RVL(LL.root, None)

if __name__ == '__main__':
    LL = LinkedList()
    LL.insert(1)
    LL.insert(-2)
    LL.insert(5)
    LL.insert(3)
    
    LL.print()
    #RevLinkedList(LL)
    IRVL(LL)
    
    print('\n\n')
    
    LL.print()
    #RevLinkedList(LL)
    IRVL(LL)
    
    print('\n\n')
    LL.print()
