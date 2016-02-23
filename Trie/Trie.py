root = {}

def insert(word):
    
    curNode = root
    
    for letter in word:
        if letter in curNode:
            curNode = curNode[letter]
        else:
            curNode[letter] = {}
            curNode = curNode[letter]

    curNode[None] = None

def search(word):
    curNode = root
    
    for letter in word:
        if letter in curNode:
            curNode = curNode[letter]
        else:
            return False

    if None in curNode.values():
        return True

    return False

