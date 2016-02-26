from heapq import *

def KMOE(L, k):
    hashMap = {}
    for num in L:

        if num not in hashMap.keys():
            hashMap[num] = 1

        else:
            hashMap[num] += 1
        
   

    kHeap = []

    for key, value in hashMap.items():
        heappush(kHeap, (-value, key)) #max heap push


    kMost = []

    while(k > 0):
        popped = heappop(kHeap)
        kMost.append((popped[1], -popped[0]))
        k -= 1

    return kMost

if __name__ == '__main__':
    L = [1, 2, 2, 1, 1, 3, 4, 3, 3, 5, 5, 5, 5]

    print(KMOE(L, 4)) 
