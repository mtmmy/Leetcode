using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {
    public class StringToInteger {
        public int MyAtoi(string str) {

            if (str.Length < 1) {
                return 0;
            }
            var integers = new List<int>();
            var result = 0;
            var positive = true;
            var hitNumber = false;
            var previousNotNumber = false;
            for (var i = 0; i < str.Length; i++) {
                var ascII = Convert.ToInt32(str[i]);

                if (ascII == 43 && hitNumber == false) {
                    positive = true;
                    if (previousNotNumber) {
                        return 0;
                    }
                    previousNotNumber = true;
                } else if (ascII == 45 && hitNumber == false) {
                    positive = false;
                    if (previousNotNumber) {
                        return 0;
                    }
                    previousNotNumber = true;
                } else if (ascII > 47 && ascII < 58) {
                    hitNumber = true;
                    integers.Add(ascII - 48);
                } else if (ascII == 32 && hitNumber == false) {
                    if (previousNotNumber) {
                        return 0;
                    }
                } else {
                    break;
                }
            }

            if (integers.Count < 1) {
                return 0;
            }

            for (var i = integers.Count - 1; i >= 0; i--) {
                var exp = (int)Math.Pow(10, integers.Count - i - 1);
                var multiply = integers[i] * exp;
                var sum = result + multiply;
                var indiResult = sum - result;
                
                if (indiResult != multiply || multiply / exp != integers[i]) {
                    return positive ? 2147483647 : -2147483648;
                }
                result = sum;
            }
            result = positive ? result : -result;
            if (result > 0 ^ positive && result != 0) {
                return positive ? 2147483647 : -2147483648;
            }

            return result;
        }
    }
}
