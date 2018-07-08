using System;
namespace Leetcode.Solutions {
    public class RotateImage {
        public void Solution (int[,] matrix) {
            var bound = matrix.GetUpperBound(0);
            var halfBound = bound / 2 + 1;

            for (int i = 0; i < halfBound; i++) {
                for (int j = i; j < bound - i; j++) {
                    SwapFour(matrix, bound, i, j);
                }
            }
        }

        void SwapFour(int[,] matrix, int bound, int i, int j) {
            var temp = matrix[i, j];
            matrix[i, j] = matrix[bound - j, i];
            matrix[bound - j, i] = matrix[bound - i, bound - j];
            matrix[bound - i, bound - j] = matrix[j, bound - i];
            matrix[j, bound - i] = temp;
        }
    }
}

//======
/* 
    //======
48. Rotate Image
    //======
  You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
    //======
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 


Let's use this matrix as an example. We start with the top-left corner and at this point, we need rotate four numbers on four coners, 5 to 11, 11 to 16, 16 to 15 and 15 to 5.
So we use a SwapFour function to accomplish this task.
In the main body of the solution, we use a nested loop to visit each starting point of SwapFour function.
However we don't need to go over all matrix. In this, example, we only need to visit, 5, 1, 9, 4 because the top-right corner (whose value is 11) has been updated when the starting point is the top-left corner.

The time complexity is O(N) where N is how many elements in the matrix even though we don't need visit every elements in the matrix, the times that SwapFour is called still growth linear depending on the size of the matrix.
    //======
        Matrix, 2D-Array
    //======
        07/06/2018
    //======
        Leetcode
    //======
https://leetcode.com/problems/rotate-image/description/
    //======
*/