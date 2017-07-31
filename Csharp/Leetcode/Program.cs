using System;
using Leetcode.Solutions;
using Leetcode.Tools;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            var obj = new Implement_strStr();
            string haystack = "mississippi";
            string needle =   "issip";

            var result = obj.StrStr(haystack, needle);

            Console.WriteLine(result);
            //Console.WriteLine("Leetcode problems!");
            Console.ReadLine();
        }
    }
}
