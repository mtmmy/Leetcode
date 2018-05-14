using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class DevideTwoIntegers {
        public int Divide(int dividend, int divisor) {

            if (divisor == 0 || (dividend == Int32.MinValue && divisor == -1)) {
                return Int32.MaxValue;
            }
            bool positive = (dividend >= 0 && divisor >= 0) || (dividend < 0 && divisor < 0);
            int quotient = 0;
            long absDividend = Math.Abs((long)dividend);
            long absDivisor = Math.Abs((long)divisor);
            
            while (absDividend >= absDivisor) {
                long temp = absDivisor;
                int multiple = 1;
                while (absDividend >= (temp << 1)) {
                    temp <<= 1;
                    multiple <<= 1;
                }
                absDividend -= temp;
                quotient += multiple;
            }

            return positive ? quotient : -quotient;
        }
    }
}
