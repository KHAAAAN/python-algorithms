#How to find K most occuring elements"
import heapq

def findKMOE(L, K):
    H = {}
    heap = [] #max heap
    for item in L:
        if item not in L:
            H[item] = 1
            heap.heappush((-1, H[item]))
        
        else:
            H[item] += 1
            heap.updatekey #figure out how to update


    for i in range(0, K):
        print(i)

        

