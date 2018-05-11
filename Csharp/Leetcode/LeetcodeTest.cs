using System;
using NUnit.Framework;
using Leetcode.Solutions;
using Leetcode.Tools;
using System.Collections.Generic;
using System.Linq;

namespace Leetcode
{
	[TestFixture]
    public class LeetcodeTest
    {
		//#1
        [Test]
        public void TwoSumTests()
        {
            TwoSum target = new TwoSum();
            int[] testAry = { 2, 7, 11, 15 };
            int targetNum = 9;
            int[] result = target.TwoSumSolution(testAry, targetNum);

            CollectionAssert.AreEqual(new[] { 0, 1 }, result);
        }

        //#2
        public void AddTwoNumbersTests()
        {
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
        [Test]
        public void LongestSubstringTests()
        {

            LongestSubstringWithoutRepeatingChars target = new LongestSubstringWithoutRepeatingChars();

            Assert.AreEqual(3, target.LengthOfLongestSubstring("abcabcbb"));
        }

        //#4
        [Test]
        public void MedianOfTwoSortedTests()
        {

            MedianOfTwoSortedArrays target = new MedianOfTwoSortedArrays();

            int[] nums1 = { 1, 2 };
            int[] nums2 = { 3, 4 };

            Assert.AreEqual(2.5, target.FindMedianSortedArrays(nums1, nums2));
        }

        //#5
        [Test]
        public void LongestPalindromicSubstringTests()
        {

            LongestPalindromicSubstring target = new LongestPalindromicSubstring();

            String result = target.LongestPalindromicSubstringSolution("babad");

            Assert.IsTrue(String.Compare("bab", result) == 1 || String.Compare("aba", result) == 1);
        }

        //#6
        [Test]
        public void ZigZagConversionTests()
        {

            ZigZagConversion target = new ZigZagConversion();

            String result = target.Convert("PAYPALISHIRING", 3);

            Assert.AreEqual("PAHNAPLSIIGYIR", result);
        }

        //#7
        [Test]
        public void ReverseIntegerTests()
        {

            ReverseInterger target = new ReverseInterger();

            Assert.AreEqual(321, target.Reverse(123));
            Assert.AreEqual(-321, target.Reverse(-123));
        }

        //#8
        [Test]
        public void StringToIntegerTests()
        {

            StringToInteger target = new StringToInteger();

            Assert.AreEqual(123, target.MyAtoi("0000123"));
            Assert.AreEqual(-123, target.MyAtoi("-0000123"));
        }

        //#9
        [Test]
        public void PalindromeNumberTests()
        {

            PalindromeNumber target = new PalindromeNumber();

            Assert.IsTrue(target.IsPalindrome(1234554321));
        }

        //#10
        [Test]
        public void RegExMatchTests()
        {

            ReqularExpressionMatching target = new ReqularExpressionMatching();

            Assert.IsFalse(target.IsMatch("aa", "a"));
            Assert.IsTrue(target.IsMatch("aa", "aa"));
            Assert.IsFalse(target.IsMatch("aaa", "aa"));
            Assert.IsTrue(target.IsMatch("aa", "a*"));
            Assert.IsTrue(target.IsMatch("aa", ".*"));
            Assert.IsTrue(target.IsMatch("ab", ".*"));
            Assert.IsTrue(target.IsMatch("aab", "c*a*b"));
        }

        //#11
        [Test]
        public void ContainerWithMostWaterTests()
        {

            ContainerWithMostWater target = new ContainerWithMostWater();
            Assert.AreEqual(12, target.MaxArea(new[] { 1, 2, 3, 4, 5, 6, 7 }));
        }

        //#12
        [Test]
        public void IntegerToRomanTests()
        {

            IntegerToRoman target = new IntegerToRoman();
            Assert.AreEqual("MMMCMXCIX", target.IntToRoman(3999));
        }

        //#13
        [Test]
        public void RomanToIntegerTests()
        {

            RomanToInteger target = new RomanToInteger();
            Assert.AreEqual(3999, target.RomanToInt("MMMCMXCIX"));
        }

        //#14
        [Test]
        public void LongestCommonPrefixTests()
        {

            LongestCommonPrefix target = new LongestCommonPrefix();
            string[] strs = new string[] { "abc", "abcd", "abcede", "abc" };

            Assert.AreEqual("abc", target.LongestCommonPrefixSolution(strs));
        }

        //#15
        [Test]
        public void ThreeSumTests()
        {

            ThreeSum target = new ThreeSum();
            int[] nums = new int[] { -1, 0, 1, 2, -1, -4 };
            IList<IList<int>> expected = new List<IList<int>>();
            expected.Add(new List<int> { -1, -1, 2 });
            expected.Add(new List<int> { -1, 0, 1 });

            CollectionAssert.AreEqual(expected, target.ThreeSumSolution(nums));
            //Assert.IsTrue(expected.SequenceEqual(target.ThreeSumSolution(nums)));
        }

        //#17
        [Test]
        public void LetterCombinationsOfPhoneTests()
        {

            LetterCombinationOfPhone target = new LetterCombinationOfPhone();
            var expected = new List<string>() { "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf" };
            var actual = target.LetterCombinations("23");

            Assert.IsTrue(expected.SequenceEqual(actual));
        }

        //#19
        [Test]
        public void RemoveNthTests()
        {

            RemoveNthNode target = new RemoveNthNode();
            ListNode listNode = new ListNode(1);
            listNode.next = new ListNode(2);
            listNode.next.next = new ListNode(3);
            listNode.next.next.next = new ListNode(4);
            listNode.next.next.next.next = new ListNode(5);

            ListNode expected = new ListNode(1);
            expected.next = new ListNode(2);
            expected.next.next = new ListNode(3);
            expected.next.next.next = new ListNode(5);

            Assert.AreEqual(expected, target.RemoveNthFromEnd(listNode, 2));
        }

        //#20
        [Test]
        public void ValidParenthesesTests()
        {

            ValidParentheses target = new ValidParentheses();
            Assert.IsTrue(target.IsValid("()(())[[]]{{}{}}"));
        }

        //#21
        [Test]
        public void MergedTwoSortedTests()
        {

            MergedTwoSortedList target = new MergedTwoSortedList();
            ListNode node1 = new ListNode(1);
            node1.next = new ListNode(3);

            ListNode node2 = new ListNode(2);
            node2.next = new ListNode(4);

            ListNode expected = new ListNode(1);
            expected.next = new ListNode(2);
            expected.next.next = new ListNode(3);
            expected.next.next.next = new ListNode(4);

            Assert.AreEqual(expected, target.MergeTwoLists(node1, node2));
        }

        //#22
        [Test]
        public void GenerateParenthesesTests()
        {

            GenerateParentheses target = new GenerateParentheses();
        }

        //#23
        [Test]
        public void MergeKSortedListsTests()
        {

            MergeKSortedLists target = new MergeKSortedLists();
            int size = 10;
            ListNode[] array = new ListNode[size];
            for (int i = 0; i < size; i++)
            {
                var node = new ListNode(2 * i);
                node.next = new ListNode(2 * i + 1);
                array[i] = node;
            }

            var result = target.MergeKLists(array);

            var expected = new ListNode(0);
            var cur = expected;
            for (int i = 1; i < 20; i++)
            {
                cur.next = new ListNode(i);
                cur = cur.next;
            }

            Assert.AreEqual(expected, result);
        }

        //#24
        [Test]
        public void SwapNodesInPairsTests()
        {

            var target = new SwapNodesInPairs();

            var test = new ListNode(0);
            var cur = test;
            for (int i = 1; i < 5; i++)
            {
                cur.next = new ListNode(i);
                cur = cur.next;
            }

            var result = target.SwapPairs(test);

            var expected = new ListNode(1);
            expected.next = new ListNode(0);
            expected.next.next = new ListNode(3);
            expected.next.next.next = new ListNode(2);
            expected.next.next.next.next = new ListNode(4);

            Assert.AreEqual(expected, result);
        }

        //#24
        [Test]
        public void ReverseNodesInKGroupTests()
        {

            var target = new ReverseNodesInKGroup();

            var head = new ListNode(-1);
            var node = new ListNode(0);
            head.next = node;
            int length = 4;
            for (int i = 1; i < length; i++)
            {
                node.next = new ListNode(i);
                node = node.next;
            }

            var result = target.ReverseKGroup(head.next, 3);

            var expected = new ListNode(2);
            expected.next = new ListNode(1);
            expected.next.next = new ListNode(0);
            expected.next.next.next = new ListNode(3);

            Assert.AreEqual(expected, result);
        }

        //#26
        [Test]
        public void RemoveDuplicateFromSortedArrayTests()
        {

            RemoveDuplicateFromSortedArray target = new RemoveDuplicateFromSortedArray();

            Assert.AreEqual(2, target.RemoveDuplicates(new int[] { 1, 1, 2 }));
        }

        //#27
        [Test]
        public void RemoveElementArrayTests()
        {

            var target = new RemoveElement();
            int[] nums = new int[] { 3, 2, 2, 3 };

            Assert.AreEqual(2, target.RemoveElementSolution(nums, 3));
            Assert.AreEqual(2, target.RemoveElementSolutionAnother(nums, 3));
        }

        //#28
        [Test]
        public void Implement_strStrTests()
        {

            var target = new Implement_strStr();
            string haystack = "mississippi";
            string needle = "issip";

            Assert.AreEqual(4, target.StrStr(haystack, needle));
        }

        //#28
        [Test]
        public void DevideTwoIntegersTests()
        {

            var target = new DevideTwoIntegers();

            Assert.AreEqual(10, target.Divide(101, 10));
            Assert.AreEqual(Int32.MaxValue, target.Divide(Int32.MinValue, -1));
            Assert.AreEqual(Int32.MinValue, target.Divide(Int32.MinValue, 1));
        }

        //#31
        [Test]
        public void NextPermutationTests()
        {

            var target = new NextPermutation();
            int[] nums = new int[] { 3, 2, 1, 3, 3, 1 };
            target.NextPermutationSolution(nums);
            CollectionAssert.AreEqual(new int[] { 3, 2, 3, 1, 1, 3 }, nums);

            nums = new int[] { 5, 4, 3, 2, 1 };
            target.NextPermutationSolution(nums);
            CollectionAssert.AreEqual(new int[] { 1, 2, 3, 4, 5 }, nums);
        }
    }
}
