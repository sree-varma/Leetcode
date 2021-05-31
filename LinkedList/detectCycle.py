"""PROBLEM NUMBER: 142- Linked List Cycle II """

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.
"""

#Solution
def detectCycle(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        out=set()
        if head==None or head.next==None:
            return None
        temp=head
        while temp:
            
            if temp not in out:
                out.add(temp)
            else:
                
                return (temp)
            temp=temp.next
        return None

# hasCycle([3,2,0,-4]) #pos=1
