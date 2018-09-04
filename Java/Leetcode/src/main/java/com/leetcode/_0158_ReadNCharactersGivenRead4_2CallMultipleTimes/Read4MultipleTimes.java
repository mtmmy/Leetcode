package com.leetcode._0158_ReadNCharactersGivenRead4_2CallMultipleTimes;

/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */
class Reader4 {
    int counter = 0;
    public int read4(char[] buffer) {
        int curr = 0;
        for (int i = 0; i < 4; ++i) {
            if (counter < 10) buffer[i] = 'a';
            else if (counter < 20) buffer[i] = 'b';
            else break;
            curr++;
            counter++;
        }
        return curr;
    }
}

public class Read4MultipleTimes extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    private int buffPtr = 0;
    private int buffCnt = 0;
    private char[] buff = new char[4];
    public int solution(char[] buf, int n) {
        int ptr = 0;
        while (ptr < n) {
            if (buffPtr == 0) {
                System.out.println(buff);
                buffCnt = read4(buff);
            }
            if (buffCnt == 0) break;
            while (ptr < n && buffPtr < buffCnt) {
                buf[ptr++] = buff[buffPtr++];
            }
            if (buffPtr >= buffCnt) buffPtr = 0;
        }
        return ptr;
    }
}