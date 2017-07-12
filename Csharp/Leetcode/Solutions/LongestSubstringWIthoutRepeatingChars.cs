using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {
    public class LongestSubstringWithoutRepeatingChars {
        public int LengthOfLongestSubstring(string s) {
            if (s.Length < 2) {
                return s.Length;
            }

            int[] array = Enumerable.Repeat(-1, 256).ToArray();

            var longest = 0;
            var m = 0;
            for (var i = 0; i < s.Length; i++) {
                var ascII = (int)s[i];
                m = Math.Max(array[ascII] + 1, m);
                array[ascII] = i;
                longest = Math.Max(longest, i - m + 1);
            }
            return longest;
        }
    }
}
