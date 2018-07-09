using System;
namespace Leetcode.Solutions {
    public class SqrtOfX {
        public int Solution(int x) {
            long r = x;
            while (r * r > x) {
                r = (r + x / r) / 2;
            }
            return (int)r;
        }
    }
}
