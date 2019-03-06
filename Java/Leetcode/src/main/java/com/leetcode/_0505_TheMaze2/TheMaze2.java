package com.leetcode._0505_TheMaze2;

import java.util.PriorityQueue;

public class TheMaze2 {
    private class Point {
        public int x, y, l;
        public Point(int x, int y, int l) {
            this.x = x;
            this.y = y;
            this.l = l;
        }
    }

    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int m = maze.length, n = maze[0].length;
        boolean visited[][] = new boolean[m][n];
        int dir[][] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        PriorityQueue<Point> queue = new PriorityQueue<>((o1, o2) -> o1.l - o2.l);
        queue.offer(new Point(start[0], start[1], 0));

        while (!queue.isEmpty()) {
            Point cur = queue.poll();
            if (visited[cur.x][cur.y]) {
                continue;
            }
            visited[cur.x][cur.y] = true;
            for (int i = 0; i < 4; i++) {
                int x = cur.x, y = cur.y, l = cur.l;
                while(x >= 0 && x < m && y >= 0 && y < n && maze[x][y] == 0) {
                    x += dir[i][0];
                    y += dir[i][1];
                    l++;
                }
                Point next = new Point(x - dir[i][0], y - dir[i][1], l - 1);
                if (next.x == destination[0] && next.y == destination[1]) {
                    return next.l;
                }
                queue.offer(next);
            }
        }
        return -1;
    }
}
