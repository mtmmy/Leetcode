import com.mycompany.leetcode.LongestValidParentheses;
import com.mycompany.leetcode.SearchForARange;
import com.mycompany.leetcode.SearchInRotatedSortedArray;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import com.mycompany.leetcode.SearchInsertPosition;
import com.mycompany.leetcode.SubstringWithConcatenationOfAllWords;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.hamcrest.CoreMatchers;
import org.junit.Assert;

public class LeetcodeTests {
    
    public LeetcodeTests() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }
    
    @Before
    public void setUp() {
    }
    
    @After
    public void tearDown() {
    }    
    
    //#30
    @Test
    public void SubstringWithConcatenationOfAllWordsTests() {
        SubstringWithConcatenationOfAllWords target = new SubstringWithConcatenationOfAllWords();
        String[] strArray = new String[]{"foo", "bar"};
        List<Integer> result = target.findSubstring("qddsfoobarewfewfbarfooffewgew", strArray);        
        Assert.assertEquals(new ArrayList<>(Arrays.asList(4, 16)), result);
    }
    
    //#32
    @Test
    public void LongestValidParenthesesTests() {
        LongestValidParentheses target = new LongestValidParentheses();
        Assert.assertEquals(6, target.longestValidParentheses("()()()"));
    }
    
    //#33
    @Test
    public void SearchInRotatedSortedArray() {
        SearchInRotatedSortedArray target = new SearchInRotatedSortedArray();
        int[] intArray = new int[]{4, 5, 6, 7, 0, 1, 2};
        int result = target.search(intArray, 1);
        Assert.assertEquals(5, result);
    }
    
    //#34
    @Test
    public void SearchForARange() {
        SearchForARange target = new SearchForARange();
        int[] result = target.searchRange(new int[]{2, 3, 4, 4, 5, 5, 6, 7, 8, 8, 8, 8, 9, 11}, 8);
        Assert.assertArrayEquals(new int[]{8, 11}, result);
    }
    
    //#35
    @Test
    public void SearchInsertPositionTests() {
        
        SearchInsertPosition target = new SearchInsertPosition();        
        int nums[] = new int[]{1, 2, 3, 4};        
        Assert.assertEquals(0, target.SearchInsert(nums, 0));
    }
}
