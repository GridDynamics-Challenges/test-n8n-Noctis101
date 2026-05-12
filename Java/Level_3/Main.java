package Level_3;

/**
 * Operation High Vantage - Level 3
 * Target Time: 45 Minutes
 */
public class Main {

    public static int[] findSteepestPath(int[][] matrix) {
    if (matrix == null || matrix.length == 0) return new int[0];

    int maxGain = -1;
    int[] steepestPath = matrix[0];

    for (int[] path : matrix) {
        int currentGain = calculateElevationGain(path);
        
        if (currentGain > maxGain) {
            maxGain = currentGain;
            steepestPath = path;
        }
    }

    return maxGain == -1 ? new int[0] : steepestPath;
}

}
