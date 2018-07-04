using System;
using System.Linq;
using System.Collections.Generic;

namespace Leetcode.Solutions {
    public class ValidSudoku {
        public bool Solution (char[,] board) {

            var rows = new List<Dictionary<char, int>>();
            var columns = new List<Dictionary<char, int>>();
            var squares = new List<Dictionary<char, int>>();

            for (int i = 0; i < 9; i++) {
                rows.Add(new Dictionary<char, int>());
                columns.Add(new Dictionary<char, int>());
                squares.Add(new Dictionary<char, int>());
            }

            int n = 0;
            foreach (var value in board) {
                int rowNo = n / 9;
                int columnNo = n % 9;

                if (value != '.') {
                    if (rows[rowNo].ContainsKey(value)) {
                        return false;
                    } else {
                        rows[rowNo].Add(value, 1);
                    }

                    // for columns
                    if (columns[columnNo].ContainsKey(value)) {
                        return false;
                    } else {
                        columns[columnNo].Add(value, 1);
                    }

                    // for squares
                    int x = rowNo / 3;
                    int y = columnNo / 3;
                    int squareIndex = x * 3 + y;

                    if (squares[squareIndex].ContainsKey(value)) {
                        return false;
                    } else {
                        squares[squareIndex].Add(value, 1);
                    }
                }
                n++;
            }

            return true;
        }
    }
}

//======
/* 
    //======
36. Valid Sudoku
    //======
  Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
    //======
        Use three lists to store states of numbers in rows, columns and sub-boxes.
        We go over the board and whenever we get a number, we check if this number has existed in the same row, column or sub-box.
        If the same number has already existed, the program returns false, Otherwise, we add the number to the corespoding row, column and sub-box.
        Since we only go over the board once, the time complexity is O(n). However we need extra space to store states for rows, columns and sub-boxes and the space complexity is O(n).
    //======
        Sudoku
    //======
        07/02/2018
    //======
        Leetcode
    //======
    https://leetcode.com/problems/valid-sudoku/description/
    //======
*/