class Stack:
    def __init__(self):
        self.__list = []
    
    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()
    
    def exists(self, name):
        if name in self.__list: return True

        return False

    def isEmpty(self):
        if len(self.__list) is 0:
            return True

    def peak(self):
        return self.__list[-1]

    def printList(self):
        for node in self.__list:
            print(node.name)

        return False

class Node:
    def __init__(self, name, edges):
        self.visited = False
        self.name = name
        self.edges = edges

    def getEdges(self):
        return self.edges    
    

class Graph:
    def __init__(self):
        self.__structure = {

            'A' : Node('A', ['B', 'C', 'E']) ,
            'B' : Node('B', ['D']) ,
            'C' : Node('C', []) ,
            'D' : Node('D', []) ,
            'E' : Node('E', ['F']) ,
            'F' : Node('F', ['A'])
    
        }

    def getNode(self, name):
        if name not in self.__structure.keys():
            return None

        return self.__structure[name]
            

def CycleExists(G, start):
    s = Stack() #initialize stack
    
    node = G.getNode(start) #get the first node
    
    if node is None: #if there's no node return
        return False

    node.visited = True #that first node is now visited

    s.push(node) #push us onto the stack
    
    if len(node.getEdges()) is 0: #if it has no where to go, there is no cycle
        return False  

    while not s.isEmpty():
        s.printList()
        input()

        edges = node.getEdges() #get the node's edges
        print(edges)

        if len(edges) is 0:
            s.pop()
            node = s.peak()
            continue

        for edge in edges:
            flag = 0
            
            destinationTo = G.getNode(edge)
            if destinationTo.visited is False: #if we have not visited
                node = destinationTo #we can break out, switch our node reference to this new node
                node.visited = True
                s.push(node)
                    
                flag = 1
                break
            
            if destinationTo.visited is True and s.exists(destinationTo.name) is True:
                return True

        if flag is 0: #all edges have been visited, pop us (node)
            s.pop() 
            node = s.peak()
         
    return False

        
    

if __name__ == '__main__':

   G = Graph()
   print(CycleExists(G, 'A'))
