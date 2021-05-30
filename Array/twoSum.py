"""PROBLEM NUMBER: 1- Two Sum """

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

#Solution
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        out=[]
            
        for i,j in enumerate(nums):
            
            if target-j in nums[i+1:]:
                out.append(i)
                out.append(nums[i+1:].index(target-j)+i+1)
                
                return(out)
                
                
#twoSum(nums=[2,7,11,15], target = 9)
