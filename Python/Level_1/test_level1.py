import pytest
from main import cleanData, findPeak

class TestLevel1:
    
    def test_cleanData_standard(self):
        assert cleanData([1200, -50, 3400, -100, 2100]) == [1200, 3400, 2100]
        
    def test_cleanData_all_negative(self):
        assert cleanData([-500, -200, -100]) == []
        
    def test_findPeak_standard(self):
        assert findPeak([1200, 3400, 2100, 5600, 4300]) == 5600
        
    def test_findPeak_plateau(self):
        assert findPeak([4000, 4000, 2500, 1000]) == 4000
