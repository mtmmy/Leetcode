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
