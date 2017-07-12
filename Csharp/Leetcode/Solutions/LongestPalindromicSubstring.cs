using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode {
    public class LongestPalindromicSubstring {
        int longest = 1;

        public string SeparateS(string s) {

            string result = ".";

            for (var i = 0; i < s.Length; i++) {
                result += s[i];
                result += ".";
            }

            return result;
        }

        public string LongestPalindromicSubstringSolution(string s) {

            var separetedString = SeparateS(s);

            var startAt = FindLongestStarts(separetedString);

            if (s.Length > 1) {
                separetedString = separetedString.Substring(startAt - longest, longest * 2);
            }
            return separetedString.Replace(".", "");
        }

        public int FindLongestStarts(string s) {

            Console.WriteLine(s);
            if (s.Length < 3) {
                return 1;
            }

            var startIndex = 0;

            for (var i = 1; i < s.Length; i++) {
                var min = Math.Min(i, s.Length - i - 1);
                for (var j = 1; j <= min; j++) {

                    if (s[i - j] == s[i + j]) {
                        if (j >= longest) {
                            longest = j;
                            startIndex = i;
                        }
                    } else {
                        break;
                    }
                }
            }
            return startIndex;
        }
    }
}
