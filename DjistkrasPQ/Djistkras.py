import PriorityQ

class Graph:
    def __init__(self):
        self.__structure = {

            'A' : [ ('B', 20), ('D', 80), ('G', 90) ] , 'B' : [ ('F', 10) ] , 
            'C' : [ ('D', 10), ('F', 50), ('H', 20) ] ,

            'D' : [ ('G', 20) ] ,

            'E' : [ ('B', 50), ('G', 30) ] ,

            'F' : [ ('C', 10), ('D', 40) ],

            'G' : [ ('A', 20) ], 

            'H' : []

        }

    def getEdges(self, vertexKey):
        return self.__structure[vertexKey]

    def getVertices(self):
        return self.__structure.keys()
    

TEST = 0
def PAUSE():
    if TEST is 1:
        input()

def Djistkras(G, start): #G is our graph, start is our starting vertex.
    shortest = {} #to keep track of our current shortest distance to that vertex from start 

    pq = PriorityQ() #initialize priority queue
    
    shortest[start] = 0 #the distance from start to start is 0, i.e 'A' to 'A' is 0

    vertices = G.getVertices() #getVertices returns all vertices in our Graph, G

    for vertex in vertices: 
        if vertex is not start:
            shortest[vertex] = float('inf') #start = 0

        pq.push(vertex, shortest[vertex]) #push all vetex and their current estimated shortest paths

    print(shortest)

    PAUSE()

    while not pq.isEmpty():
        #destinationFrom is the vertex we are coming from, and distanceFrom is the distance it took to get here so far.
        destinationFrom, distanceFrom = pq.pop() 
        print("destinationFrom, distanceFrom = ", destinationFrom, distanceFrom)

        #get all the outgoing edges along with their respective vertices
        edges = G.getEdges(destinationFrom)
       
        #we will no check all those outdoing edges
        for edge in edges:
            #destinationTo is the destination we are going to and distanceTo is the distance it takes to get there
            destinationTo, distanceTo = edge[0], edge[1] #edge is a tuple

            print("destinationTo, distanceTo = ", destinationTo, distanceTo)    
            
            distanceNew = distanceFrom + distanceTo #get the total distance from our previous distance

            if distanceNew < shortest[destinationTo]: #if our new distance is less than our old distance to that new vertex we are going to, replace
                shortest[destinationTo] = distanceNew
                
                #update priority queue with our new distance for when we come across it in our priority queue
                pq.update(destinationTo, distanceNew)
        
        PAUSE()
    
    return shortest            

if __name__ == '__main__':
    G = Graph()
    shortest = Djistkras(G, 'A') 
    print("\n\n\n\nFinal Result: ", shortest)
