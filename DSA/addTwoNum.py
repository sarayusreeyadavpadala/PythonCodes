class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        def extract(temp):
            if not temp:
                return '0'
            num=extract(temp.next)
            num=num+str(temp.val)
            return num
            
        def insert(head,num):
            for i in num:
                new=ListNode(int(i))
                if head==None:
                    head=new
                else:
                    new.next=head
                    head=new
            return head
        
        num1=extract(l1)
        num2=extract(l2)
        num=int(num1)+int(num2)
        num=str(num)
        head=None
        h=insert(head,num)
        return h
        
    def printl(self,head):
        temp=head
        while temp:
            print(temp.val,end="->")
            temp=temp.next
        print('None')
        
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)

bead=ListNode(1)
bead.next=ListNode(2)
bead.next.next=ListNode(3)
bead.next.next.next=ListNode(4)

obj=Solution()
n=obj.addTwoNumbers(head,bead)
obj.printl(n)
