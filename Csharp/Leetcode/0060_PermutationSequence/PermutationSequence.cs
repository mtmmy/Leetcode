using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class PermutationSequence {
        public string Solution(int n, int k) {

            var result = "";
            var nums = "123456789";
            var factorial = new int[n];
            for (int i = 0; i < n; i++) {
                factorial[i] = 1;
            }

            for (int i = 1; i < n; i++) {
                factorial[i] = factorial[i - 1] * i;
            }
            k -= 1;

            for (int i = n; i >= 1; i--) {
                var pos = k / factorial[i - 1];
                result += nums[pos];
                k %= factorial[i - 1];
                nums = nums.Remove(pos, 1);
            }
            return result;
        }
    }
}
