using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class PalindromeNumber {
        public bool IsPalindrome(int x) {

            if (x < 0) {
                return false;
            }
            
            var copyX = x;
            var reversedX = 0;
            while (x > 0) {
                reversedX = reversedX * 10 + x % 10;
                x /= 10;
            }
            return copyX == reversedX;
        }
    }
}
