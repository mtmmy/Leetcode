using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Leetcode.Solutions;
using Leetcode.Utils;

namespace Leetcode {
    class MainClass {
        public static void Main(string[] args) {

            var toolKit = new ToolKit();
            var target = new InorderTraversal();

            PrintResult(target.Solution(toolKit.GenerateTreeNode(new List<string>() {"1", "null", "2", "3"})));
            PrintResult(target.Solution(toolKit.GenerateTreeNode(new List<string>() { "1", "2", "3" })));
            PrintResult(target.Solution(toolKit.GenerateTreeNode(new List<string>() { "1", "2", "null", "3" })));
            PrintResult(target.Solution(toolKit.GenerateTreeNode(new List<string>() { "1", "2", "3", "4", "5", "null", "null", "null", "null", "6", "7", "null", "null", "8", "9" })));

        }

        static void PrintResult<T>(T result) {
            if (result == null) {
                Console.WriteLine("null");
            } else {
                Console.WriteLine(result);
            }
        }

        static void PrintResult<T>(IList<T> result) {
            Console.Write("[");
            Console.Write(string.Join(",", result));
            Console.Write("]\n");
        }

        static void PrintResult<T>(IList<IList<T>> result) {

            var resultString = new StringBuilder();
            var internalList = new List<string>();

            foreach (List<T> r in result) {
                var sb = new StringBuilder();
                sb.Append("[");
                sb.Append(string.Join(",", r));
                sb.Append("]");
                internalList.Add(sb.ToString());
            }

            resultString.Append("[\n");
            resultString.Append(string.Join(",\n", internalList));
            resultString.Append("\n]");

            Console.WriteLine(resultString.ToString());
        }

        static void PrintResult<T>(T[,] matrix) {
            var sb = new StringBuilder();

            int count = 0;
            var height = matrix.GetLength(0);
            var width = matrix.GetLength(1);

            sb.Append("[\n");
            foreach (T element in matrix) {
                if (count % width == 0) {
                    sb.Append("  [");
                }
                sb.Append(element.ToString());
                if (count % width == width - 1) {
                    sb.Append("],\n");
                } else {
                    sb.Append(",\t");
                }
                count++;
            }
            sb.Append("]");
            Console.WriteLine(sb.ToString());
        }
    }
}
