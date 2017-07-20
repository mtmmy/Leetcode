using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class ReverseInterger {
        public int Reverse(int x) {
            try {
                var log10 = Math.Floor(Math.Log10((double)Math.Abs(x)));
                var integers = new List<int>();
                var positive = x >= 0;

                for (var i = 0; i <= log10; i++) {
                    if (i > 0) {
                        integers.Add((int)(x / Math.Pow(10, i)) % 10);
                    } else {
                        integers.Add(x % 10);
                    }
                }

                int result = 0;
                for (var i = 0; i < integers.Count; i++) {
                    var exp = integers.Count - i - 1;

                    var multiply = (int)Math.Pow(10, exp);
                    var indiMultiple = integers[i] * multiply;
                    var sum = result + indiMultiple;
                    var indiResult = sum - result;

                    if (indiResult != indiMultiple || (indiResult) / multiply != integers[i]) {
                        return 0;
                    }
                    result = sum;
                }
                if (result > 0 ^ positive) {
                    return 0;
                }
                return result;
            } catch (OverflowException ex) {
                return 0;
            }
        }
    }
}
