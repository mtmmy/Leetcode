using System;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {
            /* test case for #1
			int[] testAry = { 2, 7, 11, 15 };
			int target = 9;
			int[] result = TwoSum.Solution(testAry, target);
			Console.WriteLine("[" + string.Join(",", result) + "]");
            */

            /* test case for #2
            ListNode number1 = new ListNode(2);
            number1.next = new ListNode(4);
            number1.next.next = new ListNode(3);

            ListNode number2 = new ListNode(5);
            number2.next = new ListNode(6);
            number2.next.next = new ListNode(4);

            ListNode result = AddTwoNumbers.Solution(number1, number2);

            Console.WriteLine(result.val + " -> " + result.next.val + " -> " + result.next.next.val);
            */

            /* test case for #3
            Console.WriteLine(LongestSubstringWIthoutRepeatingChars.Solution("abcabcbb"));
            */

            /* test case for #4
            int[] nums1 = { 1, 2 };
            int[] nums2 = { 3, 4 };
            Console.WriteLine(MedianOfTwoSortedArrays.Solution(nums1, nums2));
            */

            Console.ReadLine();
        }
    }
}
