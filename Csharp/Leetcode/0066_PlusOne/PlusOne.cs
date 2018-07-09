using System;
using System.Linq;
namespace Leetcode.Solutions
{
    public class PlusOne
    {
		public int[] Solution(int[] digits) {
   
			for (int i = digits.Length - 1; i >= 0; i--) {
				var temp = digits[i] + 1;
				if (temp < 10) {
					digits[i] = temp;
					break;
				} else {
					digits[i] = 0;
					if (i == 0) {
						int[] result = Enumerable.Repeat(0, digits.Length + 1).ToArray();
						result[0] = 1;
						return result;
					}
				}
			}
			return digits;
		}
    }
}
