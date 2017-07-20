using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class ValidParentheses {
        public bool IsValid(string s) {

            Stack<char> charStack = new Stack<char>();

            for (var i = 0; i < s.Length; i++) {
                var c = s[i];
                if (IsLeft(c)) {
                    charStack.Push(c);
                } else {
                    if (charStack.Count == 0 || !IsClose(charStack.Peek(), c)) {
                        Console.WriteLine(c);
                        return false;
                    } else {
                        charStack.Pop();
                    }
                }
            }
            return charStack.Count == 0;
        }

        public bool IsLeft(char c) {
            return c == '(' || c == '{' || c == '[';
        }

        public bool IsClose(char a, char b) {
            if (a == '(') { return b == ')'; }
            if (a == '[') { return b == ']'; }
            if (a == '{') { return b == '}'; }
            return false;
        }
    }
}
