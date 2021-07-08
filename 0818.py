from collections import deque
class Solution:
    def racecar(self, target):
        if target == 0: return 0
        queue = deque([(0,1)])
        visited = set([(0,1)])
        step = 0
        while queue:
            size = len(queue)
            step += 1
            for _ in range(size):
                pos, speed = queue.popleft()
                if pos == target:
                    return step - 1
                
                A = (pos + speed, speed * 2)
                R = (pos, -1 if speed > 0 else 1)

                if A not in visited:
                    queue.append(A)
                    visited.add(A)
                if R not in visited:
                    queue.append(R)
                    visited.add(R)
