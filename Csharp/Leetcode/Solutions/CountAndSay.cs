using System;
namespace Leetcode.Solutions
{
    public class CountAndSay
    {
		public string CountAndSaySolution(int n) {
			string result = "1";

            if (n <= 1) {
                return result;
            }

            for (int i = 2; i <= n; i++) {
                int count = 1;
				string newResult = "";
                for (int j = 1; j < result.Length; j++) {
					if (result[j] == result[j - 1]) {
						count++;
					} else {
						newResult += count.ToString() + result[j - 1];
						count = 1;
					}
                }
				newResult += count.ToString() + result[result.Length - 1];
				result = newResult;
            }

            return result;
		}
    }
}
