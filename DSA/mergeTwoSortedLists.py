class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head=None
        def insert(head,val):
            new=ListNode(val)
            if head==None:
                head=new
            else:
                temp=head
                while temp.next!=None:
                    temp=temp.next
                temp.next=new
            return head
        
        while(list1!=None and list2!=None):
            if list1.val<list2.val:
                head=insert(head,list1.val)
                list1=list1.next
            else:
                head=insert(head,list2.val)
                list2=list2.next
        while list1!=None:
            head=insert(head,list1.val)
            list1=list1.next
        while list2!=None:
            head=insert(head,list2.val)
            list2=list2.next
        return head
        
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
n=obj.mergeTwoLists(head,bead)
obj.printl(n)
            
