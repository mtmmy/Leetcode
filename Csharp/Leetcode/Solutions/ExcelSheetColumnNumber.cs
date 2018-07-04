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

//======
/* 
    //======
171. Excel Sheet Column Number
    //======
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
    //======
        It's a reverse way of #168.
    //======
        Number System
    //======
        07/02/2018
    //======
        Leetcode
    //======
    https://leetcode.com/problems/excel-sheet-column-number/description/
    //======
*/