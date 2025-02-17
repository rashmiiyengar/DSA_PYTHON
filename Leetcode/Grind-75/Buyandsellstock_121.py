#You are given an array prices where prices[i] is the price of a 
#Given stock on the ith day.

#You want to maximize your profit by choosing a single day to 
#Buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction.
#If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        min_price=float("inf")

        for price in prices:
            if price<min_price:
                min_price=price
            
            profit=price-min_price
            
            if profit>max_profit:
                max_profit=profit
        
        return max_profit

solution= Solution()
print(solution.maxProfit([7,1,5,3,6,4]))


