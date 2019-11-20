def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    for i in range(1,len(prices)):
        diff = prices[i] - prices[i-1]
        if diff >0:
            profit += diff
    
    return profit







if __name__ == '__main__':
    nums = [1, 2, 3, 4, 0, 5, 6, 7, 0]
    k = 3
    print(maxProfit(nums))