class Solution:
    # Function to search a given number in a row-column sorted matrix.
    def searchMatrix(self, mat, x):
        # Get dimensions of the matrix
        n = len(mat)      # Number of rows
        m = len(mat[0])   # Number of columns

        # Start search from the top-right corner
        row = 0
        col = m - 1

        # Perform the search
        while row < n and col >= 0:
            current = mat[row][col]
            if current == x:
                return True  # Element found
            elif current > x:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False  # Element not found
