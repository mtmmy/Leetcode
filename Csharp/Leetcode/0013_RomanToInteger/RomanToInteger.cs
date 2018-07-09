using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class RomanToInteger {
        public int RomanToInt(string s) {
            List<int> ints = new List<int>();

            foreach (var r in s) {
                if (r == 'M') {
                    ints.Add(1000);
                } else if (r == 'D') {
                    ints.Add(500);
                } else if (r == 'C') {
                    ints.Add(100);
                } else if (r == 'L') {
                    ints.Add(50);
                } else if (r == 'X') {
                    ints.Add(10);
                } else if (r == 'V') {
                    ints.Add(5);
                } else if (r == 'I') {
                    ints.Add(1);
                }
            }

            var result = 0;
            for (var i = 0; i < ints.Count; i++) {
                if (i + 1 < ints.Count && ints[i] < ints[i + 1]) {
                    ints[i] = -ints[i];
                }
                result += ints[i];
            }

            return result;
        }
    }
}
