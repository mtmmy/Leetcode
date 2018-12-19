using System;
namespace Leetcode.Solutions {
    public class ClimbingStairs {
        public int Solution(int n) {
            var waysAry = new int[2];
        
            for (int i = 0; i <= n; i++) {
                if (i < 2) {
                    waysAry[i] = 1;
                } else {
                    var temp = waysAry[1];
                    waysAry[1] = waysAry[0] + waysAry[1];
                    waysAry[0] = temp;
                }
            }
            return waysAry[1];
        }
    }
}
