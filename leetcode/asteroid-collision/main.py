from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        q = deque()
        q.append(asteroids[0])
        for i in range(1, len(asteroids)):
            while len(q) >= 0:
                if asteroids[i] > 0: 
                    q.append(asteroids[i])
                else:
                    if len(q) == 0:
                        q.append(asteroids[i])
                    elif q[-1] < 0:
                        q.append(asteroids[i])
                    elif q[-1] == -1 * asteroids[i]:
                        q.pop()
                    elif q[-1] < -1 * asteroids[i]:
                        q.pop()
                        continue
                break
        return list(q)
