using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {
    public class ZigZagConversion {
        public string Convert(string s, int numRows) {

            if (numRows < 2) {
                return s;
            }

            char[,] conversion = new char[numRows, s.Length];

            var ditchWidth = numRows - 2;
            var modTo = numRows * 2 - 2;
            for (var i = 0; i < s.Length; i++) {
                var mod = i % modTo;
                var shift = Math.Floor((double)i / modTo);
                if (mod < numRows) {
                    var y = (int)shift * (ditchWidth + 1);
                    conversion[mod, y] = s[i];
                } else {
                    var y = modTo - mod;
                    var x = (int)shift * (ditchWidth + 1) + i % (ditchWidth + 1);
                    conversion[y, x] = s[i];
                }
            }

            var result = "";
            for (var i = 0; i <= conversion.GetUpperBound(0); i++) {
                for (var j = 0; j <= conversion.GetUpperBound(1); j++) {
                    if (conversion[i, j] != '\x00') {
                        result += conversion[i, j];
                    }
                }
            }

            return result;
        }
    }
}
