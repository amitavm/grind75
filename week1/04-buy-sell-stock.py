#!/usr/bin/env python

# Leetcode Problem 121: Best Time to Buy and Sell Stock

def maxProfit(prices: list[int]) -> int:
    if not prices:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        # Update the running baseline
        min_price = min(min_price, price)
        # Update the maximum possible return
        max_profit = max(max_profit, price - min_price)

    return max_profit
