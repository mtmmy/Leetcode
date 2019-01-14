using System;
namespace Leetcode.Solutions {
    public class BestTimeToBuyAndSellStock {
        public int MaxProfit(int[] prices) {

            var minPrice = Int32.MaxValue;
            var maxProfit = 0;
        
            for (int i = 0; i < prices.Length; i++) {
                maxProfit = Math.Max(maxProfit, prices[i] - minPrice);
                minPrice = Math.Min(minPrice, prices[i]);
            }
            
            return maxProfit;
        }
    }
}