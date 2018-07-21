using System;
using System.Collections.Generic;
namespace Leetcode.Solutions {
    public class SpiralMatrix {
        public IList<int> Solution(int[,] matrix) {

            var result = new List<int>();

            int nowHeight = matrix.GetLength(0);
            int nowWidth = matrix.GetLength(1);

            int x = 0;
            int y = 0;

            while (nowHeight > 0 && nowWidth > 0) {

                if (nowHeight == 1) {
                    for (int i = 0; i < nowWidth; i++) {
                        result.Add(matrix[x, y++]);
                    }
                    break;
                }

                if (nowWidth == 1) {
                    for (int i = 0; i < nowHeight; i++) {
                        result.Add(matrix[x++, y]);
                    }
                    break;
                }

                for (int i = 0; i < nowWidth - 1; i++) {
                    result.Add(matrix[x, y++]);
                }

                for (int i = 0; i < nowHeight - 1; i++) {
                    result.Add(matrix[x++, y]);
                }

                for (int i = 0; i < nowWidth - 1; i++) {
                    result.Add(matrix[x, y--]);
                }

                for (int i = 0; i < nowHeight - 1; i++) {
                    result.Add(matrix[x--, y]);
                }

                nowHeight -= 2;
                nowWidth -= 2;

                x++;
                y++;
            }

            return result;
        }
    }
}
