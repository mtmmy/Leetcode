using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class Implement_strStr {
        public int StrStr(string haystack, string needle) {

            if (needle.Length == 0) { return 0; }
            if (haystack.Length < needle.Length) { return -1; }

            for (int i = 0; i < haystack.Length; i++) {
                if (haystack[i].Equals(needle[0])
                    && i + needle.Length - 1 < haystack.Length
                    && haystack[i + needle.Length - 1].Equals(needle[needle.Length - 1])) {

                    int j;
                    for (j = 0; j < needle.Length && haystack[i + j].Equals(needle[j]); j++) {
                    }
                    if (j == needle.Length) {                        
                        return i;
                    }
                }
            }

            return -1;
        }
    }
}
