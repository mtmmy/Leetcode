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

        //#1
        [TestMethod()]
        public void TwoSumTests() {
            TwoSum target = new TwoSum();
            int[] testAry = { 2, 7, 11, 15 };
            int targetNum = 9;
            int[] result = target.TwoSumSolution(testAry, targetNum);

            CollectionAssert.AreEqual(new[] { 0, 1 }, result);
        }

        //#2
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

            Assert.IsTrue(targetNum.Equals(target.AddTwoNumbersSolution(number1, number2)));

            //ListNode result = target.Solution(number1, number2);
        }

        //#3
        [TestMethod()]
        public void LongestSubstringTests() {

            LongestSubstringWithoutRepeatingChars target = new LongestSubstringWithoutRepeatingChars();

            Assert.AreEqual(3, target.LengthOfLongestSubstring("abcabcbb"));
        }

        //#4
        [TestMethod()]
        public void MedianOfTwoSortedTests() {

            MedianOfTwoSortedArrays target = new MedianOfTwoSortedArrays();

            int[] nums1 = { 1, 2 };
            int[] nums2 = { 3, 4 };

            Assert.AreEqual(2.5, target.FindMedianSortedArrays(nums1, nums2));
        }

        //#5
        [TestMethod()]
        public void LongestPalindromicSubstringTests() {

            LongestPalindromicSubstring target = new LongestPalindromicSubstring();

            String result = target.LongestPalindromicSubstringSolution("babad");

            Assert.IsTrue(String.Compare("bab", result) == 1 || String.Compare("aba", result) == 1);
        }

        //#6
        [TestMethod()]
        public void ZigZagConversionTests() {

            ZigZagConversion target = new ZigZagConversion();

            String result = target.Convert("PAYPALISHIRING", 3);

            Assert.AreEqual("PAHNAPLSIIGYIR", result);            
        }

        //#7
        [TestMethod()]
        public void ReverseIntegerTests() {

            ReverseInterger target = new ReverseInterger();

            Assert.AreEqual(321, target.Reverse(123));
            Assert.AreEqual(-321, target.Reverse(-123));
        }

        //#8
        [TestMethod()]
        public void StringToIntegerTests() {

            StringToInteger target = new StringToInteger();

            Assert.AreEqual(123, target.MyAtoi("0000123"));
            Assert.AreEqual(-123, target.MyAtoi("-0000123"));
        }

        //#9
        [TestMethod()]
        public void PalindromeNumberTests() {

            PalindromeNumber target = new PalindromeNumber();

            Assert.IsTrue(target.IsPalindrome(1234554321));
        }

        //#10
        [TestMethod()]
        public void RegExMatchTests() {

            ReqularExpressionMatching target = new ReqularExpressionMatching();

            Assert.IsFalse(target.IsMatch("aa", "a"));
            Assert.IsTrue(target.IsMatch("aa", "aa"));
            Assert.IsFalse(target.IsMatch("aaa", "aa"));
            Assert.IsTrue(target.IsMatch("aa", "a*"));
            Assert.IsTrue(target.IsMatch("aa", ".*"));
            Assert.IsTrue(target.IsMatch("ab", ".*"));
            Assert.IsTrue(target.IsMatch("aab", "c*a*b"));
        }
    }
}