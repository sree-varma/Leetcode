"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=[]
        i,j=0,0
        
        if len(nums1)==0:
            if len(nums2)%2==1:
                return nums2[int(len(nums2)/2)]
            else:
                return (nums2[int((len(nums2)-1)/2)]+nums2[int((len(nums2)+1)/2)])/2
        if len(nums2)==0:
            if len(nums1)%2==1:
                return nums1[int(len(nums1)/2)]
            else:
                return (nums1[int((len(nums1)-1)/2)]+nums1[int((len(nums1)+1)/2)])/2
            
        
        
        if len(nums1)>0 or len(nums2)>0:
            while len(nums)!=len(nums1)+len(nums2): 
                
                if i<len(nums1) and j<len(nums2):
                    if nums1[i]<nums2[j]:
                        nums.append(nums1[i])
                        i+=1
                        
                        

                    else:
                        
                        nums.append(nums2[j])
                        j+=1
                        
                    
                    
                    
                    
                if i>=len(nums1) and j<len(nums2):
                    nums.append(nums2[j])
                    j+=1
                if j>=len(nums2) and i<len(nums1):
                    nums.append(nums1[i])
                    i+=1
                if i>=len(nums1) and j>=len(nums2):
                    break
                
        if len(nums)%2==1:
            return nums[int(len(nums)/2)]
        else:
            return (nums[int((len(nums)-1)/2)]+nums[int((len(nums)+1)/2)])/2
