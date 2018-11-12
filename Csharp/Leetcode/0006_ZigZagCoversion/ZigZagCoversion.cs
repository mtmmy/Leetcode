using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class ZigZagConversion {
        public string Convert(string s, int numRows) {

            if (numRows == 1 || numRows >= s.Length) {
                return s;
            }
            
            string[] list = new string[numRows];
            int index = 0;
            int step = 1;
            
            foreach (char c in s) {
                list[index] += c;
                if (index == 0) {
                    step = 1;
                } else if (index == numRows - 1) {
                    step = -1;
                }
                index += step;
            }
            
            return string.Join("", list);
        }
    }
}
