class Solution:
    
    def visit(self, grid: List[List[str]], row, col):
        # mark visited
        grid[row][col] = '-1'
        
        # visit left
        if row > 0 and grid[row-1][col] == '1':
            self.visit(grid, row-1, col)
        # visit right
        if row < len(grid)-1 and grid[row+1][col] == '1':
            self.visit(grid, row+1, col)
        # visit up
        if col > 0 and grid[row][col-1] == '1':
            self.visit(grid, row, col-1)
        # visit down
        if col < len(grid[0])-1 and grid[row][col+1] == '1':
            self.visit(grid, row, col+1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if(grid[row][col] == '1'):
                    count += 1
                    self.visit(grid, row, col)
        return count
