class Solution:
    def longestValidParentheses(self, s: str) -> int:

        self.sums = [0] * len(s)
        self.inds = []
        for i in range(3 * len(s)):
            self.inds.append([])
        self.mins = []
        for i in range(len(s)):
            self.mins.append([])
            for j in range(50):
                self.mins[i].append([])
        if len(s) == 0:
            return 0
        # Computing sums
        if s[0] == ')':
            self.sums[0] = -1
        else:
            self.sums[0] = 1

        for i in range(1, len(s)):
            self.sums[i] = self.sums[i - 1]
            if s[i] == ')':
                self.sums[i] -= 1
            else:
                self.sums[i] += 1
        # Computing mins
        for i in range(len(s)):
            self.mins[i][0] = self.sums[i]
            cnt = 1
            while(i - 2 ** cnt >= 0):
                self.mins[i][cnt] = min(self.mins[i - 2 ** (cnt - 1)][cnt - 1], self.mins[i][cnt - 1])
                cnt += 1
        
        # Binary search for each element
        ans = 0
        self.inds[0].append(-1)
        for i in range(len(s)):
            sum_i = self.sums[i]
            if len(self.inds[sum_i]) > 0:
                st = len(self.inds[sum_i]) - 1
                en = 0
                mid = (en + st) // 2
                while(st - en > 1):
                    mid = (st + en) // 2
                    if self.min(self.inds[sum_i][mid], i) == sum_i:
                        ans = max(ans, i - self.inds[sum_i][mid])
                        st = mid
                    else:
                        en = mid 
                    print(st, en)
                if self.min(self.inds[sum_i][en], i) == sum_i:
                    ans = max(ans, i - self.inds[sum_i][en]) 
                if self.min(self.inds[sum_i][st], i) == sum_i: 
                    ans = max(ans, i - self.inds[sum_i][st])            
            self.inds[sum_i].append(i)
        return ans            

    def min(self, i, j):
        if i == -1:
            i = 0
        if i == j:
            return self.mins[i][0]
        x = 0
        while(j - 2 ** (x + 1) >= i):
            x += 1
        return min(self.mins[j][x], self.min(i, j - 2 ** x))
        
