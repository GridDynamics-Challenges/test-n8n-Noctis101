import pytest
from main import findSteepestPath

class TestLevel3:
    
    def test_findSteepestPath_standard(self):
        path_a = [1000, -50, 1500, 1200]
        path_b = [800, 1000, 1500, -90]
        path_c = [2000, 1000, 500]
        
        matrix = [path_a, path_b, path_c]
        
        assert findSteepestPath(matrix) == path_b
        
    def test_findSteepestPath_tie(self):
        path_a = [100, 200]
        path_b = [300, 400]
        
        matrix = [path_a, path_b]
        assert findSteepestPath(matrix) == path_a

    def test_findSteepestPath_empty_matrix(self):
        assert findSteepestPath([]) == []
