using Microsoft.VisualStudio.TestTools.UnitTesting;
using Leetcode;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Tests {
    [TestClass()]
    public class ProblemsTests {

        [TestMethod()]
        public void TwoSumTests() {
            TwoSum target = new TwoSum();
            int[] testAry = { 2, 7, 11, 15 };
            int targetNum = 9;
            int[] result = target.Solution(testAry, targetNum);

            CollectionAssert.AreEqual(new[] { 0, 1 }, result);
        }

        [TestMethod()]
        public void AddTwoNumbersTests() {
            ListNode number1 = new ListNode(2);
            number1.next = new ListNode(4);
            number1.next.next = new ListNode(3);

            ListNode number2 = new ListNode(5);
            number2.next = new ListNode(6);
            number2.next.next = new ListNode(4);

            ListNode targetNum = new ListNode(7);
            targetNum.next = new ListNode(0);
            targetNum.next.next = new ListNode(8);

            AddTwoNumbers target = new AddTwoNumbers();

            Assert.IsTrue(targetNum.Equals(target.Solution(number1, number2)));

            //ListNode result = target.Solution(number1, number2);
        }

        [TestMethod()]
        public void LongestSubstringTests() {

            LongestSubstringWIthoutRepeatingChars target = new LongestSubstringWIthoutRepeatingChars();

            Assert.AreEqual(3, target.Solution("abcabcbb"));
        }

        [TestMethod()]
        public void MedianOfTwoSortedTests() {

            MedianOfTwoSortedArrays target = new MedianOfTwoSortedArrays();

            int[] nums1 = { 1, 2 };
            int[] nums2 = { 3, 4 };

            Assert.AreEqual(2.5, target.Solution(nums1, nums2));
        }
    }
}