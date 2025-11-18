rom collections import deque

class Solution:
    def cutOffTree(self, forest):
        if not forest or not forest[0]:
            return -1

        rows, cols = len(forest), len(forest[0])
        
        # Step 1: Collect all trees with height > 1
        trees = sorted((h, r, c) for r in range(rows) for c in range(cols) if forest[r][c] > 1)

        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0
            visited = [[False]*cols for _ in range(rows)]
            queue = deque([(sr, sc, 0)])
            visited[sr][sc] = True

            while queue:
                r, c, d = queue.popleft()
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return d + 1
                        visited[nr][nc] = True
                        queue.append((nr, nc, d + 1))
            return -1

        total_steps = 0
        sr = sc = 0

        for height, tr, tc in trees:
            steps = bfs(sr, sc, tr, tc)
            if steps == -1:
                return -1
            total_steps += steps
            sr, sc = tr, tc

        return total_steps
