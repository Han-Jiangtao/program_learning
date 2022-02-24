class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for _idx in range(len(grid[0])):
            now_ball = [0, _idx]
            flag = True
            for _cnt in range(len(grid)):
                #print(_idx, now_ball)
                line = grid[now_ball[0]][now_ball[1]]
                if line == 1:
                    if now_ball[1] + line == len(grid[0]) or grid[now_ball[0]][now_ball[1] + 1] == -1:
                        ans.append(-1)
                        flag = False
                        break
                if line == -1:
                    if now_ball[1] + line < 0 or grid[now_ball[0]][now_ball[1] - 1] == 1:
                        ans.append(-1)
                        flag = False
                        break
                now_ball = [now_ball[0] + 1, now_ball[1] + line]
            if flag:
                ans.append(now_ball[1])
        return ans
