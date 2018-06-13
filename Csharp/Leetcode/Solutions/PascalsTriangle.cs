using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class PascalsTriangle {
        public IList<IList<int>> Generate(int numRows) {
            var result = new List<IList<int>>(numRows);

            for (int i = 1; i <= numRows; i++) {
                if (i == 1) {
                    result.Add(new List<int> { 1 });
                } else if (i == 2) {
                    result.Add(new List<int> { 1, 1 });
                } else {
                    var prevRow = result[i - 2];
                    var thisRow = new List<int>(new int[i]);
                    thisRow[0] = 1;
                    thisRow[i - 1] = 1;

                    for (int j = 1; j < i - 1; j++) {
                        thisRow[j] = prevRow[j - 1] + prevRow[j];
                    }
                    result.Add(thisRow);
                }
            }

            return result;
        }
    }
}
