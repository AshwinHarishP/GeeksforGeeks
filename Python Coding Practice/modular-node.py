#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def modularNode(head, k):
    #function should return the modular Node
    #if no such node is present then return -1
    
    #finding length of linked list
    
    temp = head
    length = 0
    while temp != None:
        length += 1
        temp = temp.next
    
    #Finding largest value
    for i in range(1, length + 1):
        digit = length + 1 - i
        if digit % k == 0:
            largest = digit
            break
    else:
        return -1
    #Returning largest node data
    
    pos = head
    j = 1
    while pos != None:
        if j == largest:
            return pos.data
        j += 1
        pos = pos.next



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
        
 

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        k=int(input())
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        print(modularNode(a.head,k))


# } Driver Code Ends
