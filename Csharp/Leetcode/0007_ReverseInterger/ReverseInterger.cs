using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class ReverseInterger {
        public int Reverse(int x) {
            var result = 0;
            while (x != 0) {            
                var digit = x % 10;
                x /= 10;
                
                if (result > Int32.MaxValue / 10 || result < Int32.MinValue / 10) {
                    return 0;
                }
                result = result * 10 + digit;  
            }
            return result;
        }
    }
}
