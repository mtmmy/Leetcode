using System;
using NUnit.Framework;
using Leetcode.Solutions;
using Leetcode.Tools;
using System.Collections.Generic;
using System.Linq;

namespace Leetcode {
    [TestFixture]
    public class LeetcodeTest {
        //#1
        [Test]
        public void TwoSumTests() {
            TwoSum target = new TwoSum();
            int[] testAry = { 2, 7, 11, 15 };
            int targetNum = 9;
            int[] result = target.TwoSumSolution(testAry, targetNum);

            CollectionAssert.AreEqual(new[] { 0, 1 }, result);
        }

        //#2
        [Test]
        public void AddTwoNumbersTests() {
            var number1 = new ListNode(new[] { 2, 4, 3 });
            var number2 = new ListNode(new[] { 5, 6, 4 });
            AddTwoNumbers target = new AddTwoNumbers();

            Assert.AreEqual("7, 0, 8", target.AddTwoNumbersSolution(number1, number2).ToString());
        }

        //#3
        [Test]
        public void LongestSubstringTests() {
            LongestSubstringWithoutRepeatingChars target = new LongestSubstringWithoutRepeatingChars();

            Assert.AreEqual(3, target.LengthOfLongestSubstring("abcabcbb"));
        }

        //#4
        [Test]
        public void MedianOfTwoSortedTests() {
            MedianOfTwoSortedArrays target = new MedianOfTwoSortedArrays();
            int[] nums1 = { 1, 2 };
            int[] nums2 = { 3, 4 };

            Assert.AreEqual(2.5, target.FindMedianSortedArrays(nums1, nums2));
        }

        //#5
        [Test]
        public void LongestPalindromicSubstringTests() {
            LongestPalindromicSubstring target = new LongestPalindromicSubstring();
            String result = target.LongestPalindromicSubstringSolution("babad");

            Assert.IsTrue(String.Compare("bab", result) == 1 || String.Compare("aba", result) == 1);
        }

        //#6
        [Test]
        public void ZigZagConversionTests() {
            ZigZagConversion target = new ZigZagConversion();
            String result = target.Convert("PAYPALISHIRING", 3);

            Assert.AreEqual("PAHNAPLSIIGYIR", result);
        }

        //#7
        [Test]
        public void ReverseIntegerTests() {
            ReverseInterger target = new ReverseInterger();

            Assert.AreEqual(321, target.Reverse(123));
            Assert.AreEqual(-321, target.Reverse(-123));
        }

        //#8
        [Test]
        public void StringToIntegerTests() {
            StringToInteger target = new StringToInteger();

            Assert.AreEqual(123, target.MyAtoi("0000123"));
            Assert.AreEqual(-123, target.MyAtoi("-0000123"));
        }

        //#9
        [Test]
        public void PalindromeNumberTests() {

            PalindromeNumber target = new PalindromeNumber();

            Assert.IsTrue(target.IsPalindrome(1234554321));
        }

        //#10
        [Test]
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

        //#11
        [Test]
        public void ContainerWithMostWaterTests() {
            ContainerWithMostWater target = new ContainerWithMostWater();

            Assert.AreEqual(12, target.MaxArea(new[] { 1, 2, 3, 4, 5, 6, 7 }));
        }

        //#12
        [Test]
        public void IntegerToRomanTests() {
            IntegerToRoman target = new IntegerToRoman();

            Assert.AreEqual("MMMCMXCIX", target.IntToRoman(3999));
        }

        //#13
        [Test]
        public void RomanToIntegerTests() {
            RomanToInteger target = new RomanToInteger();

            Assert.AreEqual(3999, target.RomanToInt("MMMCMXCIX"));
        }

        //#14
        [Test]
        public void LongestCommonPrefixTests() {
            LongestCommonPrefix target = new LongestCommonPrefix();
            string[] strs = new string[] { "abc", "abcd", "abcede", "abc" };

            Assert.AreEqual("abc", target.LongestCommonPrefixSolution(strs));
        }

        //#15
        [Test]
        public void ThreeSumTests() {
            ThreeSum target = new ThreeSum();
            int[] nums = new int[] { -1, 0, 1, 2, -1, -4 };
            IList<IList<int>> expected = new List<IList<int>>();
            expected.Add(new List<int> { -1, -1, 2 });
            expected.Add(new List<int> { -1, 0, 1 });

            CollectionAssert.AreEqual(expected, target.ThreeSumSolution(nums));
        }

        //#17
        [Test]
        public void LetterCombinationsOfPhoneTests() {
            LetterCombinationOfPhone target = new LetterCombinationOfPhone();
            var expected = new List<string>() { "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf" };
            var actual = target.LetterCombinations("23");

            Assert.IsTrue(expected.SequenceEqual(actual));
        }

        //#19
        [Test]
        public void RemoveNthTests() {
            RemoveNthNode target = new RemoveNthNode();
            var listNode = new ListNode(new[] { 1, 2, 3, 4, 5 });

            Assert.AreEqual("1, 2, 3, 5", target.RemoveNthFromEnd(listNode, 2).ToString());
        }

        //#20
        [Test]
        public void ValidParenthesesTests() {
            ValidParentheses target = new ValidParentheses();

            Assert.IsTrue(target.IsValid("()(())[[]]{{}{}}"));
        }

        //#21
        [Test]
        public void MergedTwoSortedTests() {
            MergedTwoSortedList target = new MergedTwoSortedList();
            var node1 = new ListNode(new[] { 1, 3 });
            var node2 = new ListNode(new[] { 2, 4 });

            Assert.AreEqual("1, 2, 3, 4", target.MergeTwoLists(node1, node2).ToString());
        }

        //#22
        [Test]
        public void GenerateParenthesesTests() {

            GenerateParentheses target = new GenerateParentheses();
            var expected = new List<string>() { "((()))", "(()())", "(())()", "()(())", "()()()" };

            CollectionAssert.AreEqual(expected, target.GenerateParenthesis(3));
        }

        //#23
        [Test]
        public void MergeKSortedListsTests() {
            MergeKSortedLists target = new MergeKSortedLists();
            int size = 10;
            ListNode[] array = new ListNode[size];
            for (int i = 0; i < size; i++) {
                var node = new ListNode(new[] { 2 * i, 2 * i + 1 });
                array[i] = node;
            }
            var result = target.MergeKLists(array);

            Assert.AreEqual("0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19", result.ToString());
        }

        //#24
        [Test]
        public void SwapNodesInPairsTests() {
            var target = new SwapNodesInPairs();
            var test = new ListNode(new[] { 0, 1, 2, 3, 4 });
            var result = target.SwapPairs(test);

            Assert.AreEqual("1, 0, 3, 2, 4", result.ToString());
        }

        //#24
        [Test]
        public void ReverseNodesInKGroupTests() {
            var target = new ReverseNodesInKGroup();
            var head = new ListNode(new[] { 0, 1, 2, 3 });
            var result = target.ReverseKGroup(head, 3);

            Assert.AreEqual("2, 1, 0, 3", result.ToString());
        }

        //#26
        [Test]
        public void RemoveDuplicateFromSortedArrayTests() {
            RemoveDuplicateFromSortedArray target = new RemoveDuplicateFromSortedArray();

            Assert.AreEqual(2, target.RemoveDuplicates(new int[] { 1, 1, 2 }));
        }

        //#27
        [Test]
        public void RemoveElementArrayTests() {
            var target = new RemoveElement();
            int[] nums = new int[] { 3, 2, 2, 3 };

            Assert.AreEqual(2, target.RemoveElementSolution(nums, 3));
            Assert.AreEqual(2, target.RemoveElementSolutionAnother(nums, 3));
        }

        //#28
        [Test]
        public void Implement_strStrTests() {
            var target = new Implement_strStr();
            string haystack = "mississippi";
            string needle = "issip";

            Assert.AreEqual(4, target.StrStr(haystack, needle));
        }

        //#28
        [Test]
        public void DevideTwoIntegersTests() {
            var target = new DevideTwoIntegers();

            Assert.AreEqual(10, target.Divide(101, 10));
            Assert.AreEqual(Int32.MaxValue, target.Divide(Int32.MinValue, -1));
            Assert.AreEqual(Int32.MinValue, target.Divide(Int32.MinValue, 1));
        }

        //#31
        [Test]
        public void NextPermutationTests() {
            var target = new NextPermutation();
            int[] nums = new int[] { 3, 2, 1, 3, 3, 1 };
            target.NextPermutationSolution(nums);
            CollectionAssert.AreEqual(new int[] { 3, 2, 3, 1, 1, 3 }, nums);

            nums = new int[] { 5, 4, 3, 2, 1 };
            target.NextPermutationSolution(nums);
            CollectionAssert.AreEqual(new int[] { 1, 2, 3, 4, 5 }, nums);
        }

        //#38
        [Test]
        public void CountAndSayTests() {
            var target = new CountAndSay();
            var result = target.CountAndSaySolution(10);
            Assert.AreEqual("13211311123113112211", result);
        }

        //#53
        [Test]
        public void MaximumSubarrayTests() {
            var target = new MaximumSubarray();
            Assert.AreEqual(6, target.MaxSubArray(new[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
        }

        //#58
        [Test]
        public void LengthOfTheLastWordTests() {
            var target = new LengthOfLastWord();
            Assert.AreEqual(5, target.Solution("Hello world"));
        }

        //#66
        [Test]
        public void PlusOneTests() {
            var target = new PlusOne();

            CollectionAssert.AreEqual(new[] { 1 }, target.Solution(new[] { 0 }));
            CollectionAssert.AreEqual(new[] { 1, 0 }, target.Solution(new[] { 9 }));
            CollectionAssert.AreEqual(new[] { 4, 3, 2, 2 }, target.Solution(new[] { 4, 3, 2, 1 }));
            CollectionAssert.AreEqual(new[] { 1, 0, 0, 0, 0 }, target.Solution(new[] { 9, 9, 9, 9 }));
        }

        //#67
        [Test]
        public void AddBinaryTests() {
            var target = new AddBinary();

            Assert.AreEqual("100", target.Solution("11", "1"));
            Assert.AreEqual("110001", target.Solution("101111", "10"));
        }

        //#69
        [Test]
        public void SqrtOfXTests() {
            var target = new SqrtOfX();

            Assert.AreEqual(0, target.Solution(0));
            Assert.AreEqual(1, target.Solution(1));
            Assert.AreEqual(1, target.Solution(2));
            Assert.AreEqual(8, target.Solution(64));
            Assert.AreEqual(15, target.Solution(255));
            Assert.AreEqual(16, target.Solution(257));
            Assert.AreEqual(46340, target.Solution(2147395600));
        }

        //#70
        [Test]
        public void ClimbingStairsTests() {
            var target = new ClimbingStairs();

            Assert.AreEqual(0, target.Solution(0));
            Assert.AreEqual(2, target.Solution(2));
            Assert.AreEqual(8, target.Solution(5));
            Assert.AreEqual(1836311903, target.Solution(45));
        }

        //#83
        [Test]
        public void RemoveDuplicatesFromSortedListTests() {
            var target = new RemoveDuplicatesFromSortedList();
            var listNode = new ListNode(new[] { 1, 1, 2, 2, 3, 3 });

            Assert.AreEqual("1, 2, 3", target.Solution(listNode).ToString());
        }
    }
}
