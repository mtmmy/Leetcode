using System;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class PascalsTriangle {
        public IList<IList<int>> Generate(int numRows) {
            var result = new List<IList<int>>();
        
            for (int i = 0; i < numRows; i++) {
                if (i == 0) {
                    result.Add(new List<int> { 1 });
                } else if (i == 1) {
                    result.Add(new List<int> { 1, 1 });
                } else {
                    var thisRow = new List<int>(new int[i + 1]);
                    thisRow[0] = 1;
                    thisRow[i] = 1;

                    for (int j = 1; j < i; j++) {
                        thisRow[j] = result[i - 1][j - 1] + result[i - 1][j];
                    }
                    result.Add(thisRow);
                }
            }

            return result;
        }
    }
}
