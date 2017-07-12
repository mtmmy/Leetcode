using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {
    public class ReqularExpressionMatching {
        public bool IsMatch(string s, string p) {

            var m = s.Length;
            var n = p.Length;
            var dp = new bool[m + 1, n + 1];

            for (var i = 0; i <= dp.GetUpperBound(0); i++) {
                for (var j = 0; j <= dp.GetUpperBound(1); j++) {
                    dp[i, j] = false;
                }
            }

            dp[0, 0] = true;
            for (var i = 0; i <= dp.GetUpperBound(0); i++) {
                for (var j = 1; j <= dp.GetUpperBound(1); j++) {
                    if (p[j - 1] != '*' && p[j - 1] != '.') {
                        if (i > 0 && s[i - 1] == p[j - 1] && dp[i - 1, j - 1]) {
                            dp[i, j] = true;
                        }
                    } else if (p[j - 1] == '.') {
                        if (i > 0 && dp[i - 1, j - 1]) {
                            dp[i, j] = true;
                        }
                    } else if (j > 1) {
                        if (dp[i, j - 1] || dp[i, j - 2]) { //check 0 or 1 element
                            dp[i, j] = true;
                        } else if (i > 0 && dp[i - 1, j] && (p[j - 2] == s[i - 1] || p[j - 2] == '.')) { //check multiple elements
                            dp[i, j] = true;
                        }
                    }
                }
            }

            return dp[m, n];
        }
    }
}
