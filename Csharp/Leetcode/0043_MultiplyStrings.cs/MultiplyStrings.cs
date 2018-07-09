using System;
using System.Text;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class MultiplyStrings {
        public string Solution(string num1, string num2) {

            var length1 = num1.Length;
            var length2 = num2.Length;
            var size = length1 + length2;
            var tempArray = new int[size];

            for (int i = 0; i < length1; i++) {
                for (int j = 0; j < length2; j++) {
                    tempArray[size - 2 - i - j] += (num1[i] - '0') * (num2[j] - '0');
                }
            }

            var carry = 0;
            for (int i = 0; i < size; i++) {
                tempArray[i] += carry;
                carry = tempArray[i] / 10;
                tempArray[i] = tempArray[i] % 10;
            }

            while (tempArray[size - 1] == 0) {
                size--;
                if (size <= 0) {
                    return "0";
                }
            }

            var result = new StringBuilder();

            for (int i = size - 1; i >= 0; i--) {
                result.Append(tempArray[i].ToString());
            }

            return result.ToString();
        }
    }
}

//======
/* 
    //======
43. Multiply Strings
    //======
  Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
    //======
    First we create an array to store values of each places and the length of the array is num1.Length + num2.Length. 
    For example, 99 * 999 = 98901, the digits of the product will be shorter or equal to the sum of length of multiplier and multiplicant.
    
    We use a nested loop to multiply just like we do multiply on the paper and store the value to the temp array without carrying.
    For example, when we multiply 16 by 15, the temp array be like the following:
    [ 30, 11, 1, 0 ]
    From the left to right are ones place, tens place, hundreds place and keep increasing.
    comparing to the multiplication on the paper:
          1   6
        X 1   5
     ------------
          5  30
       1  6
     ------------
       1 11  30
    remember we ignore carry at this moment.

    Next step we calculate the carry so the temp array will become:
    [ 0, 4, 2, 0 ]

    The last pare we need convert the temp array to string and remove all leading zeros.
    We iterate backward for the temp array and keep reducing its size if the value of the index is zero until we meet a non-zero number or the size of the array becomes zero.
    If the size is zero in the end we simply return "0". Other wise we append the elements of the array backward to the string of the result.

    The time complexity of this problem is O(N^2) because we have to use a nested loop to go over two strings of numbers.
    //======
        String, Big Numbers
    //======
        07/05/2018
    //======
        Leetcode
    //======
            https://leetcode.com/problems/multiply-strings/description/
    //======
*/