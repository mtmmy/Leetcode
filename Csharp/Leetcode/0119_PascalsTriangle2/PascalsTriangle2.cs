using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class PascalsTriangle2 {
        public IList<int> GetRow(int rowIndex) {
            var prevRow = new List<int> { 1 };
            var curRow = new List<int> { 1 };

            for (int i = 0; i < rowIndex; i++) {
                curRow.Insert(0, 1);
                if (prevRow.Count > 1) {
                    for (int j = 1; j < curRow.Count - 1; j++) {
                        curRow[j] = prevRow[j - 1] + prevRow[j];
                    }
                }
                prevRow = new List<int>(curRow);
            }

            return curRow;
        }
    }
}
