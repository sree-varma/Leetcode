"""PROBLEM NUMBER: 344- Reverse String """

"""
Write a function that reverses a string. The input string is given as an array of characters s.
"""


#Solution

def reverseString(s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        k=0
        if len(s)%2==0:
            k=int(len(s)/2)
        if len(s)%2!=0:
            k=int(len(s)/2+1)
        i=0
        while i<k:
            temp=s[i]
            s[i]=s[len(s)-i-1]
            s[len(s)-i-1]=temp
            i=i+1
