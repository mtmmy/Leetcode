using System;
namespace Leetcode.Solutions {
    public class ClimbingStairs {
        public int Solution(int n) {
            var waysAry = new int[n + 1];

            if (n <= 2) {
                return n;
            }

            for (int i = 0; i <= n; i++) {
                if (i <= 2) {
                    waysAry[i] = i;
                } else {
                    waysAry[i] = waysAry[i - 1] + waysAry[i - 2];
                }
            }
            return waysAry[n];
        }
    }
}
