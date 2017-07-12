using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {
    public class PalindromeNumber {
        public bool IsPalindrome(int x) {

            if (x < 0) {
                return false;
            }

            if (x < 10) {
                return true;
            }

            var integers = new List<int>();
            while (x > 0) {
                integers.Add(x % 10);
                x /= 10;
            }

            var count = integers.Count;
            for (var i = 0; i < count; i++) {
                if (i > count - i - 1) {
                    break;
                }
                if (integers[i] != integers[count - i - 1]) {
                    return false;
                }
            }
            return true;
        }
    }
}
