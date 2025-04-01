
def valid_mountain_array():
    heights = [int(x) for x in input().split()]
    
    if len(heights) < 3:
        return False
    
    n = len(heights)
    i = 0
    
    # Подъем
    while i < n - 1 and heights[i] < heights[i + 1]:
        i += 1
    
    if i == 0 or i == n - 1:
        return False
    
    # Спуск
    while i < n - 1 and heights[i] > heights[i + 1]:
        i += 1
    
    return i == n - 1

print(valid_mountain_array())