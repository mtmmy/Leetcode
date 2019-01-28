using System;
namespace Leetcode.Solutions {
    public class ExcelSheetColumnNumber {
        public int Solution(string s) {

            var length = s.Length;
            var result = 0;

            for (int i = length - 1; i >= 0; i--) {
                var place = length - i - 1;
                int powOf26 = Convert.ToInt32(Math.Pow(26, place));
                int digitInDecimal = (Convert.ToInt32(Convert.ToChar(s[i])) - 64) * powOf26;
                result += digitInDecimal;
            }

            return result;
        }
    }
}