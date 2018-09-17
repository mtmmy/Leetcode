package com.leetcode._0759_EmployeeFreeTime;

import com.leetcode.utils.Interval;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class EmployeeFreeTime {
    public List<Interval> solution(List<List<Interval>> schedule) {
        int n = 0;
        for (List<Interval> list : schedule) {
            n += list.size();
        }

        int[] starts = new int[n];
        int[] ends = new int[n];
        int i = 0;

        for (List<Interval> list : schedule) {
            for (Interval l : list) {
                starts[i] = l.start;
                ends[i++] = l.end;
            }
        }

        Arrays.sort(starts);
        Arrays.sort(ends);

        List<Interval> result = new ArrayList<>();
        for (i = 0; i < n - 1; i++) {
            if (ends[i] < starts[i + 1]) {
                result.add(new Interval(ends[i], starts[i + 1]));
            }
        }

        return result;
    }

    public List<Interval> solution2(List<List<Interval>> schedule) {
        List<Interval> intervals = new ArrayList<>();
        List<Interval> result = new ArrayList<>();

        for (List<Interval> inter : schedule) {
            intervals.addAll(inter);
        }

        intervals.sort((i1, i2) -> i1.start - i2.start);
        Interval temp = intervals.get(0);

        for (Interval i : intervals) {
            if (temp.end < i.start) {
                result.add(new Interval(temp.end, i.start));
                temp = i;
            } else {
                temp = temp.end < i.end ? i : temp;
            }
        }
        return result;
    }
}
