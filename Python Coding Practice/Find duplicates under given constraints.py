# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Stack = []
        Sum_1 = ""
        Sum_2 = ""
        
        if l1 == None:
            Sum_1 = ""
        elif l2 == None:
            Sum_2 = ""

        else:
            temp_1 = l1

            while temp_1 != None:
                Stack.append(temp_1.val)
                temp_1 = temp_1.next

            while len(Stack) != 0:
                Sum_1 += str(Stack.pop)

        print(Sum_1)
