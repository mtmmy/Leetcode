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