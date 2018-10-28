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