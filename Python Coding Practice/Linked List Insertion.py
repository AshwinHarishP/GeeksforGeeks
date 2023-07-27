'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        new_node = Node(x)
        
        #Case 1: head is None
        
        if head == None:
            head = new_node
            return head
        
        #Insertnig new node at beginning
        new_node.next = head
        head = new_node
        return head
    
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        new_node = Node(x)
         
        #Case1: If head is None
        if head == None:
            head = new_node
            head.next = None
            return head
            
        #Traversing to last
        temp = head
        while temp.next != None:
            temp = temp.next
        
        #Inserting node at last
        temp.next = new_node
        new_node.next = None
        return head
            
             




#{ 
 # Driver Code Starts
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
    print()

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a=LinkedList()
        
        nodes_info=list(map(int,input().split()))
        for i in range(0,len(nodes_info)-1,2):
            if(nodes_info[i+1]==0):
                a.head = Solution().insertAtBegining(a.head,nodes_info[i])
            else:
                a.head = Solution().insertAtEnd(a.head,nodes_info[i])
        printList(a.head)

 
# } Driver Code Ends
