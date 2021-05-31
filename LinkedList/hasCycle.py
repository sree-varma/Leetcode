"""PROBLEM NUMBER: 141- Linked List Cycle """

"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

#Solution
def hasCycle(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        out=set()
        if head==None or head.next==None:
            return False
        temp=head
        while temp:
            if temp not in out:
                out.add(temp)
            else:
                return True
            temp=temp.next
        return False


# hasCycle([3,2,0,-4]) #pos=1
