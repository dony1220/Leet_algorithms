class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return sum(nums[::2])

#10번 배열 파티션1

#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하자
#ex) [1,4,3,2] -> 출력 4가 된다는데
#min(1,4) + min(2,3) = 3 요런식


#이게 2n개로 이루어진 리스트이기 때문에, 결과적으로 sort하고나면 홀수 번째 친구들이 제일 작은놈들이란 말이지 ㅇㅈ?
# -> 그니까 결과적으로 홀수 번째 친구들만 다 더하면 되겠지 인덱스로 따지면 짝수번째 친구들 ㅇㅇ