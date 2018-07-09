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

//======
/* 
    //======
168. Excel Sheet Column Title
    //======
   Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
    //======
    We can consider it as base-26 number system (but not exactly), where A is 0 and Z is 25.
    However, there is a slightly different from a real number system which is when the number carries over, the new digit start from 0 (A in base-26).
    So we need to minus one every time we reach the new digit.

    The time complexity is O(1). The input is fixed 32-bit integer and the loop only executes 7 times when the value is the largest which is 2^31.
    //======
        Number System
    //======
        07/01/2018
    //======
        Leetcode
    //======
    https://leetcode.com/problems/excel-sheet-column-title/description/
    //======
*/