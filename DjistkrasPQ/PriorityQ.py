import heapq

class PriorityQ():
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item)) 

    def pop(self):
        priority, item = heapq.heappop(self.heap)
        return (item, priority)

    def isEmpty(self):
        if len(self.heap) is 0:
            return True

        return False

    def update(self, key, value):
        for i in range(0, len(self.heap)):
            if key == self.heap[i][1]:
                self.heap[i] = (value, key)
                heapq.heapify(self.heap)

if __name__ == '__main__':
    #test code here
    pq = PriorityQueue()
    pq.push('A', 10)
    pq.push('B', 5)
    pq.push('C', 6)
    print(pq.isEmpty())
    print(pq.pop())
    print(pq.pop())
    print(pq.pop())
    print(pq.isEmpty())
