'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20    
-1000 <= matrix[i][j] <= 1000
'''

# With use of a help matrix
def rotate(matrix):
    """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    row = []
    rotated_matrix = []
    
    for j in range(n):
        for i in range(n):
            row.append(matrix[i][j])
        row.reverse()
        rotated_matrix.append(row[:])
        row = []
        
    matrix = rotated_matrix
    return matrix

def rotateInPlace(matrix):
    """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    
    # Transpose the matrix in place
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row in place
    for i in range(n):
        matrix[i].reverse()
    
    return matrix
        

# Some Test cases
if __name__ == "__main__":
    
    matrix1 = [[1,2,3],
               [4,5,6],
               [7,8,9]]
    output1 = [[7,4,1],
               [8,5,2],
               [9,6,3]]
    
    matrix2 = [[5,1,9,11],
               [2,4,8,10],
               [13,3,6,7],
               [15,14,12,16]]
    output2 = [[15,13,2,5],
               [14,3,4,1],
               [12,6,8,9],
               [16,7,10,11]]
    
    matrix3 = []
    output3 = []
    
    # Examples
    input = [
        (matrix1, output1),
        (matrix2, output2),
        (matrix3, output3)
    ]

    for idx, (matrix, expected) in enumerate(input):
        print("\nExample", idx, ":")
        print("Input:", matrix)
        print("Output:", rotateInPlace(matrix))
        print("Expected:", expected)