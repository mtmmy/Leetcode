using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class LetterCombinationOfPhone {
        public IList<string> LetterCombinations(string digits) {
            var result = new List<string>();

            if (digits.Length == 0 || digits.Contains("0") || digits.Contains("1")) {
                return result;
            }

            string[] dict = new string[] { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
            FindLetterCombo(digits, 0, dict, new StringBuilder(new string(' ', digits.Length)), result);
            return result;
        }

        public void FindLetterCombo(string digits, int index, string[] dict, StringBuilder combo, List<string> result) {

            if (index == digits.Length) {
                result.Add(combo.ToString());
                return;
            }

            string letter = dict[digits[index] - '0'];
            for (var i = 0; i < letter.Length; i++) {
                combo[index] = letter[i];
                FindLetterCombo(digits, index + 1, dict, combo, result);
            }
        }
    }
}
