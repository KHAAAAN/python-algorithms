def FindMaxWidth(root):
    if root is None:
        return 0

    q.put(root)

    maxWidth = 0

    while not q.empty():
        curWidth = q.qsize()

        if curWidth > maxWidth:
            maxWidh = curWidth

        while curWidth > 0:
            curNode = q.get()
            
            if curNode.left is not None:
                q.put(curNode.left)

            if curNode.right is not None:
                q.put(curNode.right)

            curWidth -= 1

    return maxWidth
