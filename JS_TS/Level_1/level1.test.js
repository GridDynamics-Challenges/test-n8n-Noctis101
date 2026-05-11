const { cleanData, findPeak } = require('./index');

describe('Level 1 - Data Cleaning', () => {
    test('Removes negative glitches', () => {
        expect(cleanData([1200, -50, 3400, -100, 2100])).toEqual([1200, 3400, 2100]);
    });

    test('Handles edge case of entirely corrupted data', () => {
        expect(cleanData([-500, -200, -100])).toEqual([]);
    });
});

describe('Level 1 - Peak Finding', () => {
    test('Finds the highest peak', () => {
        expect(findPeak([1200, 3400, 2100, 5600, 4300])).toBe(5600);
    });

    test('Handles duplicate peak values', () => {
        expect(findPeak([4000, 4000, 2500, 1000])).toBe(4000);
    });
});
