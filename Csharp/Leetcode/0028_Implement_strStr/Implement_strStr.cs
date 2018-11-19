using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class Implement_strStr {
        public int StrStr(string haystack, string needle) {

            int startIndex = -1;

            if (needle.Length == 0) { return 0; }
            if (haystack.Length < needle.Length) { return -1; }

            int i = 0;
            while (i + needle.Length - 1 < haystack.Length) {
                if (haystack.Substring(i, needle.Length) == needle) {
                    return i;
                }
                i++;
            }

            return -1;
        }
    }
}
