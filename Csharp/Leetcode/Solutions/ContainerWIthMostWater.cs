using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Leetcode.Solutions {
    public class ContainerWithMostWater {
        public int MaxArea(int[] height) {

            int l = height.Length;
            int i = 0;
            int j = l - 1;
            int max = 0;
            while (i < j) {
                max = Math.Max(max, Math.Min(height[i], height[j]) * (j - i));

                if (height[i] < height[j]) {
                    i++;
                } else {
                    j--;
                }
            }
            return max;
        }
    }
}
