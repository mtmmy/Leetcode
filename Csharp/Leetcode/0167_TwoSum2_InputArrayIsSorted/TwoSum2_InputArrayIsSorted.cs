using System;
namespace Leetcode.Solutions {
    public class TwoSum2_InputArrayIsSorted {
        public int[] Solution (int[] numbers, int target) {
            var result = new int[2];

            // O(N)
            int i = 0;
            int j = numbers.Length - 1;

            while (i < j) {
                var twoSum = numbers[i] + numbers[j];
                if (twoSum == target) {
                    result[0] = i + 1;
                    result[1] = j + 1;
                    break;
                }
                if (twoSum > target) {
                    j--;
                } else {
                    i++;
                }
            }

            return result;
        }
    }
}