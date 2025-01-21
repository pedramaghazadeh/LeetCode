class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        nm = len(arr)
        
        row_ind = [0] * (nm + 1)
        col_ind = [0] * (nm + 1)
        
        row = [0] * len(mat)
        col = [0] * len(mat[0])

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                row_ind[mat[r][c]] = r
                col_ind[mat[r][c]] = c

        for ind in range(nm):
            color = arr[ind]
            row[row_ind[color]] += 1
            col[col_ind[color]] += 1
            if row[row_ind[color]] == len(mat[0]) or col[col_ind[color]] == len(mat):
                return ind