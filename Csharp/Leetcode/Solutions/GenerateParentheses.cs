using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class GenerateParentheses {
        public IList<string> GenerateParenthesis(int n) {

            var allCombos = new List<string>();
            var combo = new StringBuilder();
            FindParenthesis(n, 0, 0, combo, allCombos);
            return allCombos;
        }

        void FindParenthesis(int n, int nleft, int nright, StringBuilder combo, List<string> allCombos) {

            if (nleft == n && nright == n) {
                allCombos.Add(combo.ToString());
                return;
            }

            if (nleft < n) {
                combo.Append("(");
                FindParenthesis(n, nleft + 1, nright, combo, allCombos);
                combo.Length--;

            }

            if (nright < nleft) {
                combo.Append(")");
                FindParenthesis(n, nleft, nright + 1, combo, allCombos);
                combo.Length--;
            }
        }
    }
}
