using System;
namespace Leetcode.Solutions {
    public class BestTimeToBUyAndSellStock2 {
        public int Solution (int[] prices) {
            var total = 0;
            for (int i = 1; i < prices.Length; i++) {
                if (prices[i] > prices[i - 1]) {
                    total += prices[i] - prices[i - 1];
                }
            }
            return total;
        }
    }
}
