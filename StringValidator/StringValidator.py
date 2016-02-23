import unittest

class Stack():
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        if len(self.__list) is 0:
            return None

        return self.__list.pop()
    
    def isEmpty(self):
        if len(self.__list) is 0:
            return True

        return False

    def peak(self):
        if len(self.__list) is 0:
            return None

        return self.__list[-1]

def StringValidator(s):
    flag = True
    match = { '{': '}', '(':')' , '[':']' }

    stack = Stack()

    for ch in s:
        if ch in match.keys():
            stack.push(ch)
        
        elif ch in match.values():
            if stack.peak() == None or  match[stack.peak()] != ch:
                return False

            stack.pop()
               

    if not stack.isEmpty():
        flag = False

    return flag
        

class TestStringValidator:

    def testEmptyString(self):
        self.assertFalse(StringValidator(""))

    def testLeftUnbalanced(self):
        self.assertFalse(StringValidator(r"())"))

    def testRightUnbalanced(self):
        self.assertFalse(StringValidator("())"))

    def testLetterLeft(self):
        self.assertTrue(StringValidator(r"a(aa())"))


    def testLetterRight(self):
        self.assertTrue(StringValidator(r"(()aa)a"))

if __name__=='__main__':
    unittest.main()






























