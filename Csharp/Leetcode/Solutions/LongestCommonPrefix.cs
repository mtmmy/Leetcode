using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {
    public class LongestCommonPrefix {
        public string LongestCommonPrefixSolution(string[] strs) {

            if (strs.Length == 0) {
                return "";
            }

            int compareTo = -1;
            int shortestStr = 99999999;
            var bound = 99999999;

            for (var i = 0; i < strs.Length; i++) {
                if (strs[i].Length < shortestStr) {
                    compareTo = i;
                    shortestStr = strs[i].Length;
                }
            }

            if (shortestStr == 0) {
                return "";
            }

            for (var i = 0; i < strs.Length; i++) {
                for (var j = 0; j < bound; j++) {
                    if (strs[i][j] != strs[compareTo][j]) {
                        shortestStr = j;
                        compareTo = i;
                    }
                    bound = Math.Min(shortestStr, bound);
                }
            }

            return strs[compareTo].Substring(0, bound);
        }
    }
}
