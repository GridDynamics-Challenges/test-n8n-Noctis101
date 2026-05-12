package Level_2;

/**
 * Operation High Vantage - Level 2
 * Target Time: 30 Minutes
 */
public class Main {
  
    public static int[] cleanData(int[] arr) {
        if (arr == null) return new int[0];
        
        return java.util.Arrays.stream(arr).filter(a -> a >= 0).toArray();
    }

    public static int findPeak(int[] arr) {
        if (arr == null || arr.length == 0) return 0;
        
        return java.util.Arrays.stream(arr).max().orElse(0);
    }

    public static int calculateElevationGain(int[] arr) {
        if (arr == null || arr.length < 2) return 0;

        int totalGain = 0;
        Integer lastValid = null;

        for (int altitude : arr) {
            if (altitude >= 0) {
                if (lastValid != null && altitude > lastValid) {
                    totalGain += (altitude - lastValid);
                }
                lastValid = altitude;
            }
        }
        return totalGain;
    }
}
