using System;
namespace Leetcode.Solutions {
    public class BestTimeToBuyAndSellStock {
        public int MaxProfit(int[] prices) {

            var i = 0;
            var curLowIndex = 0;
            var curHighIndex = 0;
            var maxProfit = 0;

            while (i < prices.Length) {
                bool changed = false;
                if (prices[i] < prices[curLowIndex]) {
                    curLowIndex = i;
                    changed = true;
                }

                if (prices[i] > prices[curHighIndex]) {
                    curHighIndex = i;
                    changed = true;
                }

                if (curHighIndex < curLowIndex) {
                    curHighIndex = curLowIndex;
                }

                if (changed) {
                    maxProfit = Math.Max(maxProfit, prices[curHighIndex] - prices[curLowIndex]);
                }
                i++;
            }

            return maxProfit;

            // Kadane's Algorithm
            //int maxCur = 0, maxSoFar = 0;
            //for (int i = 1; i < prices.Length; i++) {
            //    maxCur = Math.Max(0, maxCur += prices[i] - prices[i - 1]);
            //    maxSoFar = Math.Max(maxCur, maxSoFar);
            //    Console.WriteLine("maxCur: " + maxCur + ", maxSoFar: " + maxSoFar);
            //}
            //return maxSoFar;
        }
    }
}

//======
/* 
    //======
        #121 Best Time to Buy and Sell Stock
    //======
        Say you have an array for which the ith element is the price of a given stock on day i.

        If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

        Note that you cannot sell a stock before you buy one.

        Example 1:
        Input: [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                     Not 7-1 = 6, as selling price needs to be larger than buying price.
        Example 2:
        Input: [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transaction is done, i.e. max profit = 0.
    //======
        We use a loop to traverse the array of prices and we can resolve the problem with O(n).
        In the loop, we need to remember the indices of the lowest price and the highest price. 
        And if there is a new low prices at the right hand side of the current highest price, we need reset the index of the current highest price because we can buy a stock than sell it.
        Once the index of the current highest price or the current lowest prices changes, we calculate their diiference and compare to the old maximum profit.
        In the end of the loop, we get the maximum profit.
        
    //======
        Array, Index, Loop
    //======
        05/13/2018
    //======
        Leetcode
    //======
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
    //======
*/