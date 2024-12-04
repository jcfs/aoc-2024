data = [line.strip() for line in open('d4.in').readlines()]

directions = [
        (0, 1),  
        (1, 0),  
        (1, 1),  
        (1, -1), 
        (0, -1), 
        (-1, 0), 
        (-1, -1),
        (-1, 1)  
    ]

def find_count_in_matrix(grid, word, x, y):
    r, c = len(grid), len(grid[0])

    def is_valid_direction(dx, dy):
        return all(
            0 <= x + i * dx < r and 0 <= y + i * dy < c and grid[x + i * dx][y + i * dy] == word[i]
            for i in range(len(word))
        )

    return sum(is_valid_direction(dx, dy) for dx, dy in directions)

def part1():
    r = len(data)
    c = len(data[0])

    count = 0
    for i in range(r):
        for j in range(c):
            count += find_count_in_matrix(data, 'XMAS', i, j)
                
    print(count)

def part2():
    r = len(data)
    c = len(data[0])

    count = 0
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if data[i][j] == 'A':
                d1 = (data[i - 1][j - 1], data[i + 1][j + 1])
                d2 = (data[i - 1][j + 1], data[i + 1][j - 1])

                if d1 in (('M', 'S'), ('S', 'M')) and d2 in (('M', 'S'), ('S', 'M')):
                    count += 1
    print(count)

part1()
part2()
