class MinStack(object):

    def __init__(self):
        self.l=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.l.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.l.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.l)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()