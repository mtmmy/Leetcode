using System;
using System.Collections.Generic;
using System.Linq;

namespace Leetcode.Solutions {
    public class GroupAnagrams {
        public IList<IList<string>> Solution(string[] strs) {
            
            var keyResult = new Dictionary<string, IList<string>>();

            foreach (string s in strs) {
                var count = Enumerable.Repeat(0, 26).ToList();
                foreach (char c in s) {
                    count[c - 'a']++;
                }
                string key = "";

                for (int i = 0; i < count.Count; i++) {
                    char c = Convert.ToChar('a' + i);
                    key += new string(c, count[i]);
                }
                if (keyResult.ContainsKey(key)) {
                    keyResult[key].Add(s);
                } else {
                    keyResult.Add(key, new List<string> { s });
                }
            }

            return keyResult.Values.ToList();
        }
    }
}
