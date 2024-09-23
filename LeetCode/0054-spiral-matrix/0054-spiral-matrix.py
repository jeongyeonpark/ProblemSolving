class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x_max = len(matrix[0])
        y_max = len(matrix)
        result = [matrix[0][0]]
        v = 0
        visited = set()
        visited.add((0,0))

        x = 0
        y = 0
        direction = 'right'
        while v < (x_max*y_max)-1:
            if direction == 'right':
                x+=1
            elif direction == 'left':
                x-=1
            elif direction == 'down':
                y+=1
            elif direction == 'up':
                y-=1
            
            if (x,y) in visited:
                if direction == 'up':
                    y+=1
                    x+=1
                    direction = 'right'
                elif direction == 'down':
                    y-=1
                    x-=1
                    direction = 'left'
                elif direction == 'right':
                    x-=1
                    y+=1
                    direction = 'down'
                elif direction == 'left':
                    x+=1
                    y-=1
                    direction = 'up'
            else:
                if x>x_max-1:
                    x-=1
                    y+=1
                    direction = 'down'
                elif x<0:
                    x+=1
                    y-=1
                    direction = 'up'
                elif y>y_max-1:
                    y-=1
                    x-=1
                    direction = 'left'

            result.append(matrix[y][x])
            visited.add((x,y))
            v+=1

        return result