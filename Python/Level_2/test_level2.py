import pytest
from main import calculateElevationGain, cleanData

class TestLevel2:
    
    def test_calculateElevationGain_standard(self):
        assert calculateElevationGain([1000, -50, 1500, 1200, -100, 1600]) == 900
        
    def test_calculateElevationGain_no_climb(self):
        assert calculateElevationGain([2000, 1500, -99, 1000]) == 0

    def test_calculateElevationGain_single_point(self):
        assert calculateElevationGain([1000, -50, -100]) == 0
