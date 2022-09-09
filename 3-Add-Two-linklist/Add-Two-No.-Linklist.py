# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c=0
        self.head=None
        def neww(data):
    
            if self.head==None:
                self.head=ListNode(data)
            else:
                cru=self.head
                while(cru.next!=None):
                    cru=cru.next
                d=ListNode(data)
                cru.next=d
            return
        while(l1!=None or l2!=None):
            a=0
            b=0
            if (l1!=None):
                a=l1.val
                l1=l1.next
            if l2!=None:
                b=l2.val
                l2=l2.next
            su=a+b
            if c!=0:
                su+=c
                c=0
            if su>9:
                c=su//10
                su=su%10
            neww(su)
        if c!=0:
            neww(c)
        return self.head
