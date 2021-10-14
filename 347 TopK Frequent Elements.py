from typing import List
from collections import deque

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        dictN = {}
        
        result = []
        count = 0
        if len(nums)==k:
            return nums
        if len(nums)>1:
            x = nums[1]
        while len(nums)>=1:
            
            n = nums.pop()
            if len(nums)==0:
                if n==x:
                    count += 1
                    dictN[n]= count
                else: dictN[n]= 1
                break
                
            m= nums[-1]
            count += 1
            dictN[n]= count
            print("n====",n)
            print("m=====",m)
            if (n!=m):
                
                count=0
            
            print("====dictN===")
            print(dictN)

        for i in range(0,k):
            key = max(dictN, key = dictN.get)
            dictN.pop(key)
            result.append(key)
        return result

s = Solution()

nums = [3,0,1,0]
k = 1
print("=========================")
print(s.topKFrequent(nums,k))
