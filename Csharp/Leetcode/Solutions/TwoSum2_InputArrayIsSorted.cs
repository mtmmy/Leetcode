using System;
namespace Leetcode.Solutions {
    public class TwoSum2_InputArrayIsSorted {
        public int[] Solution (int[] numbers, int target) {
            var result = new int[2];

            // O(NlogN)
            //for (int i = 0; i < numbers.Length; i++) {
            //    if (numbers[i] <= target) {
            //        for (int j = i + 1; j < numbers.Length; j++) {
            //            if (numbers[i] + numbers[j] == target) {
            //                result[0] = i + 1;
            //                result[1] = j + 1;
            //            } else if (numbers[i] + numbers[j] > target) {
            //                break;
            //            }
            //        }
            //    }
            //}

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

//======
/* 
    //======
167. Two Sum II - Input array is sorted
    //======
   Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    //======
        There are two solutions.
        
        The first one is brute-force solution which is inefficent and costs O(NlogN).
        
        The second one costs only O(N). We use two pins that one of them points to the beginning of the number array and the other points the end of the array.
        If the sum of two numbers that two pins point to equals to the target number, it's the result.
        When the sum is smaller than the target, we move the pins that is from the beginning to right and when the sum is greater than the target, we move the pins that is from the end to left.
        If there are no mathced result, the loop will end when two pins meet.
    //======
        TwoSum
    //======
        07/02/2018
    //======
        Leetcode
    //======
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
    //======
*/