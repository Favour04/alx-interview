function generatePascalTriangle(numRows) {
    if (numRows === 0) return [];
    if (numRows === 1) return [[1]];
    
    const triangle = [[1]];  // Initialize with the first row

    for (let i = 1; i < numRows; i++) {
        const row = [1];  // Start each row with 1
        const prevRow = triangle[i - 1];
        
        for (let j = 1; j < i; j++) {
            row.push(prevRow[j - 1] + prevRow[j]);
        }
        
        row.push(1);  // End each row with 1
        triangle.push(row);
    }

    return triangle;
}

// Example usage:
console.time('generatePascalTriangle');
const result = generatePascalTriangle(10);
console.timeEnd('generatePascalTriangle');
console.log(result);
