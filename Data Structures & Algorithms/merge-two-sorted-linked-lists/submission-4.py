# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1==None and list2==None:
            return None

        array = []
        
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                array.append(list1.val)
                list1 = list1.next
            else:
                array.append(list2.val)
                list2 = list2.next

        while list1!=None:
            array.append(list1.val)
            list1 = list1.next

        while list2!=None:
            array.append(list2.val)
            list2 = list2.next
        
        res = ListNode(array[0])
        start = res
        for i in range(1,len(array)):
            res.next = ListNode(array[i])
            res = res.next
        
        return start

                