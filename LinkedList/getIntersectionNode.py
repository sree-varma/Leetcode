"""PROBLEM NUMBER: 160. Intersection of Two Linked Lists """

"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

It is guaranteed that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.
"""

#Solution
def getIntersectionNode(headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp1=headA
        temp2=headB
        if (not temp1 or not temp2 ):
            return -1
          
        # Continue until we find intersection node
        while (temp1 and temp2 and temp1 != temp2):
            
            temp1 = temp1.next
            temp2 = temp2.next

            # If we get intersection node
            if (temp1 == temp2):
                return temp1

            # If one of them reaches end
            if (not temp1):
                temp1 = headB

            if (not temp2):
                temp2 = headA

        return current1

# getIntersectionNode([4,1,8,4,5], [5,6,1,8,4,5]) #intersectVal = 8  skipA = 2, skipB = 3


# Reference: https://www.geeksforgeeks.org/find-intersection-point-of-two-linked-lists-without-finding-the-length/
