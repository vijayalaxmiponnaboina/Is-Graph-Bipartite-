from collections import deque 
class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        q=deque()
        for i in range(n):
            if color[i]==-1:
                color[i]=0
                q.append(i)
                while q:
                    front=q.popleft()
                    for ne in graph[front]:
                        if color[ne] == -1:
                            color[ne]=1-color[front]
                            q.append(ne)
                        elif color[ne]==color[front]:
                            return False
        return True                  