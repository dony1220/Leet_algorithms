#나눗셈을 하지않고, O(n)에 풀이해야함.ㄹㅇ

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        #조합으로 못푸나? combination
        #빈리스트에 담을거랑, 초반 곱, 나중 곱 이렇게 나눠서 ㄱ
        f = [1]
        e = [1]
        
        for i in range(len(nums)-1):
            f.append(f[-1] * nums[i])
        for i in range(len(nums)-1, 0, -1):
            e.insert(0, e[0] * nums[i])
        for i in range(len(nums)):
            result.append(f[i] * e[i])
        return result

#o(n)은 아니지만 2중 for문으로도 가는ㅇ하지않나?
#ex)

#
# p=[1] * len(nums) [1로 다 초기화 시켜놓고]

# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i!=j:
#             p[i] *= nums[j]
#     return p
        