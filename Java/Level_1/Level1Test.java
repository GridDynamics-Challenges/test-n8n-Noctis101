package Level_1;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Level1Test {

    @Test
    public void testCleanDataStandard() {
        int[] input = {1200, -50, 3400, -100, 2100};
        int[] expected = {1200, 3400, 2100};
        assertArrayEquals(expected, Main.cleanData(input));
    }

    @Test
    public void testCleanDataAllNegative() {
        int[] input = {-500, -200, -100};
        int[] expected = {};
        assertArrayEquals(expected, Main.cleanData(input));
    }

    @Test
    public void testFindPeakStandard() {
        int[] input = {1200, 3400, 2100, 5600, 4300};
        assertEquals(5600, Main.findPeak(input));
    }

    @Test
    public void testFindPeakPlateau() {
        int[] input = {4000, 4000, 2500, 1000};
        assertEquals(4000, Main.findPeak(input));
    }
}
