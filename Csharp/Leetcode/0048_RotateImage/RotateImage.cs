using System;
namespace Leetcode.Solutions {
    public class RotateImage {
        public void Solution (int[,] matrix) {
            var n = matrix.GetUpperBound(0);
            var halfN = n / 2 + 1;

            for (int i = 0; i < halfN; i++) {
                for (int j = i; j < n - i; j++) {
                    SwapFour(matrix, n, i, j);
                }
            }
        }

        void SwapFour(int[,] matrix, int n, int i, int j) {
            var temp = matrix[i, j];
            matrix[i, j] = matrix[n - j, i];
            matrix[n - j, i] = matrix[n - i, n - j];
            matrix[n - i, n - j] = matrix[j, n - i];
            matrix[j, n - i] = temp;
        }
    }
}