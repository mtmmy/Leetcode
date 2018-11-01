# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

## Description

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

Example 2:

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Solution

We use a loop to traverse the array of prices and we can resolve the problem with O(n). In the loop, we need to remember the indices of the lowest price and the highest price. And if there is a new low prices at the right hand side of the current highest price, we need reset the index of the current highest price because we can buy a stock than sell it. Once the index of the current highest price or the current lowest prices changes, we calculate their diiference and compare to the old maximum profit. In the end of the loop, we get the maximum profit.

There is another solution called Kadane's Algothm takes O(n) as well. This algorithm uses current maximum (maxCur) and maximum so for (maxSoFar) to track the profit. maxCur indicates how much profit we get at the current index. To get this value, we keep adding the profit from the previous maxCur, and store it if it's greater than zero. And if our maxCur is greater than maxSoFar, we have a new high of profit and we keep the profit.

## Related Topics

[Array](https://leetcode.com/tag/array/) , [Dynamic Programming](https://leetcode.com/tag/dynamic-programming/) 

## Similar Questions

[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/), [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/), [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/), [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/), [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
