using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class StringToInteger {
        public int MyAtoi(string str) {

            str = str.Trim(' ');
        
            if (str.Length == 0) {
                return 0;
            }        
            
            int sign = 1;
            
            if (!Char.IsDigit(str[0])) {
                if (str[0] == '+') {
                    sign = 1;
                } else if (str[0] == '-') {
                    sign = -1;
                } else {
                    return 0;
                }
                str = str.Substring(1);
            }
            
            long result = 0;
            
            foreach (char c in str) {
                if (!Char.IsDigit(c)) {
                    break;
                }            
                result = result * 10 + (c - '0');
                if (result * sign > int.MaxValue) {
                    return int.MaxValue;
                }
                if (result * sign < int.MinValue) {
                    return int.MinValue;
                }
            }
            
            return (int)result * sign;
        }
    }
}
