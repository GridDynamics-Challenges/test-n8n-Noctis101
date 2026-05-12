package Level_1;

/**
 * Operation High Vantage - Level 1
 * Target Time: 15 Minutes
 */
public class Main {

    /**
     * Takes an array of altitude integers.
     * Returns a new array with all negative numbers removed.
     */
    public static int[] cleanData(int[] arr) {
        if (arr == null) return new int[0];

        return Arrays.stream(arr)
                     .filter(altitude -> altitude >= 0)
                     .toArray();
    }

    /**
     * Takes an array of cleaned altitude integers.
     * Returns the highest altitude.
     */
    public static int findPeak(int[] arr) {
        if (arr == null || arr.length == 0) return 0;

        return Arrays.stream(arr).max().orElse(0);
    }
}
