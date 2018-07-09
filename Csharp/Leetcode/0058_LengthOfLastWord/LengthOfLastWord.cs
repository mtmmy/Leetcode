using System;
namespace Leetcode.Solutions
{
    public class LengthOfLastWord
    {
		public int Solution(string s) {

			if (s.Length == 0) {
				return 0;
			}

			int length = 0;

			for (int i = s.Length - 1; i >= 0; i--) {
				if (s[i] != ' ') {
					length++;
				} else {
					if (length != 0) {
						break;
					}
				}
			}

			return length;
		}
    }
}
