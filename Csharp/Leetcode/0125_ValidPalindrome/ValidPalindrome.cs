using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class ValidPalindrome {
        public bool IsPalindrome(string s) {
            var i = 0;
            var j = s.Length - 1;

            s = s.ToLower();
            while (i <= j) {
                if (!Char.IsLetterOrDigit(s[i])) {
                    i++;
                    continue;
                }

                if (!Char.IsLetterOrDigit(s[j])) {
                    j--;
                    continue;
                }


                if (s[i] != s[j]) {
                    return false;
                }
                i++;
                j--;
            }
            return true;
        }
    }
}
