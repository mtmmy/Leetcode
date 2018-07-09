using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class IntegerToRoman {
        public string IntToRoman(int num) {
            string result = "";

            var M = Math.Floor((double)num / 1000);
            num = num % 1000;
            var D = Math.Floor((double)num / 500);
            num = num % 500;
            var C = Math.Floor((double)num / 100);
            num = num % 100;
            var L = Math.Floor((double)num / 50);
            num = num % 50;
            var X = Math.Floor((double)num / 10);
            num = num % 10;
            var V = Math.Floor((double)num / 5);
            var I = num % 5;

            for (var i = 0; i < M; i++) {
                result += "M";
            }

            if (C == 4) {
                if (D > 0) {
                    result += "CM";
                } else {
                    result += "CD";
                }
            } else {
                if (D > 0) {
                    result += "D";
                }
                for (var i = 0; i < C; i++) {
                    result += "C";
                }
            }

            if (X == 4) {
                if (L > 0) {
                    result += "XC";
                } else {
                    result += "XL";
                }
            } else {
                if (L > 0) {
                    result += "L";
                }
                for (var i = 0; i < X; i++) {
                    result += "X";
                }
            }

            if (I == 4) {
                if (V > 0) {
                    result += "IX";
                } else {
                    result += "IV";
                }
            } else {
                if (V > 0) {
                    result += "V";
                }
                for (var i = 0; i < I; i++) {
                    result += "I";
                }
            }

            return result;
        }
    }
}
