#나눗셈을 하지않고, O(n)에 풀이해야함.ㄹㅇ

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        s = 1
        for i in range(0, len(nums)):
            result.append(s)
            s *= nums[i]
        s = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= s
            s*=nums[i]
        return result
        
        