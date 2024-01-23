class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        cur_sum = 0
        #가격이 최대일때를 확인하기위해 0으로
        #현재 가격 
        for i in range(len(prices)-1):
            cur_sum += prices[i+1] - prices[i]
            #근데 여기서 만약에 0보다 작다면 그냥 
            #다시 0으로 초기화 시켜주면 될 거 같은데
            if cur_sum < 0:
                cur_sum = 0
            max_price = max(max_price, cur_sum)
        return max_price
        