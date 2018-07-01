using System;
namespace Leetcode.Solutions {
    public class AddBinary {
        public string Solution(string a, string b) {

            var longerLength = Math.Max(a.Length, b.Length);
            char[] result = new char[longerLength];

            var charAryA = a.ToCharArray();
            var charAryB = b.ToCharArray();

            Array.Reverse(charAryA);
            Array.Reverse(charAryB);

            bool carry = false;

            for (int i = 0; i < longerLength; i++) {
                if (i < charAryA.Length && i < charAryB.Length) {
                    char charA = charAryA[i];
                    char charB = charAryB[i];

                    if (carry) {
                        if (charA == '1' && charB == '1') {
                            carry = true;
                            result[i] = '1';
                        } else if (charA == '1' || charB == '1') {
                            carry = true;
                            result[i] = '0';
                        } else {
                            carry = false;
                            result[i] = '1';
                        }
                    } else {
                        if (charA == '1' && charB == '1') {
                            carry = true;
                            result[i] = '0';
                        } else if (charA == '1' || charB == '1') {
                            carry = false;
                            result[i] = '1';
                        } else {
                            carry = false;
                            result[i] = '0';
                        }
                    }
                } else {
                    char theChar = charAryA.Length > charAryB.Length ? charAryA[i] : charAryB[i];

                    if (carry) {
                        if (theChar == '1') {
                            carry = true;
                            result[i] = '0';
                        } else {
                            carry = false;
                            result[i] = '1';
                        }
                    } else {
                        carry = false;
                        result[i] = theChar;
                    }
                }
            }

            if (carry) {
                var carryResult = new char[longerLength + 1];

                for (int i = 0; i < longerLength; i++) {
                    carryResult[i] = result[i];
                }

                carryResult[carryResult.Length - 1] = '1';
                Array.Reverse(carryResult);
                return new string(carryResult);
            }

            Array.Reverse(result);

            return new string(result);
        }
    }
}

//======
/* 
    //======
        #67 Add Binanry
    //======
        Given two binary strings, return their sum (also a binary string).
        The input strings are both non-empty and contains only characters 1 or 0.
    //======
        First, reverse the character arrays so that they can align on the first place which makes us easier to sum up digit by digit.
        Sum up two numbers digit by digit and remember carry over to the next place if there is a carryover.
        Reverse back to the correct number.

        We need character arrays to store reversed numbers, so the space complexity is O(n).
        We use a loop to sum up two numbers bit by bit, and the executing time of the loop depends on the longer number. The time complexity is O(n).
        And we also have 3 reversing steps. The time complexity of resersing is O(n) as well.
        So the total time complexity is still O(n).
    //======
        Binary Number
    //======
        05/13/2018
    //======
        Leetcode
    //======
        https://leetcode.com/problems/add-binary/description/
    //======
*/