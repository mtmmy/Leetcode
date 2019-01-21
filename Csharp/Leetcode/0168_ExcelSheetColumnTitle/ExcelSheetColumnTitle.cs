using System;
using System.Text;
namespace Leetcode.Solutions {
    public class ExcelSheetColumnTitle {
        public string Solution(int n) {
            if (n < 1) {
                return "";
            }

            StringBuilder result = new StringBuilder("");
            var divisor = n - 1;
            var quotient = Int32.MaxValue;
            var remainder = 0;
            var letters = 1;

            while (quotient != 0) {
                
                if (letters != 1) {
                    divisor -= 1;
                }

                quotient = divisor / 26;
                remainder = divisor % 26;

                string letter = Convert.ToChar(65 + remainder).ToString();
                result = result.Insert(0, letter);

                divisor = quotient;
                letters++;
            }

            return result.ToString();
        }
    }
}