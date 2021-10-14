from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        m = len(grid)
        n = len(grid[0])
        queue = deque([[0,0]])
        searched = set()
        count = 0
        # if (len(grid) ==1 and len(grid[0])==0):
        #     if
        print("=========")
        while len(queue)>0:
            head = queue.popleft()
            x = head[0]
            y = head[1]
            print("lllllllll")               
            for q in head:
                print("x=",x, "\ty=",y, q)
                if q not in searched:
                    if (grid[x][y] == "1" and x<m and y<n):  
                        if (grid[x][y+1]=="1"):
                            queue.append([x,y+1])     
                        if (grid[x+1][y]=="1"):
                            queue.append([x+1,y])
                        else:
                            count +=1
                            
                        searched.add(q)
            if (x+2)<m: 
                queue = deque([[x+2,y]])                        
     
        return count

s = Solution()
#grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(s.numIslands(grid))
