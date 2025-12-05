def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    lines: list[list[str]] = []

    while line:
        lines.append([x for x in line])
        line = file.readline().strip()

    word = "XMAS"

    def part1():
        direction = [
            (-1, -1),(0, -1),(1, -1),
            (-1,  0),        (1,  0),
            (-1,  1),(0,  1),(1,  1)
        ]

        def add_direction(x: int, y: int, dir: int):
            new_dir = direction[dir]
            return (x + new_dir[0], y + new_dir[1])

        def rec(x: int, y: int, idx: int, dir: int):
            if (x < 0 or x > len(lines[0]) - 1 or y < 0 or y > len(lines) - 1):
                return False
            letter = lines[y][x]
            if letter == word[idx]:
                if idx == len(word) - 1:
                    return True
                x, y = add_direction(x, y, dir)
                return rec(x, y, idx + 1, dir)
            else:
                return False

        res = 0
        for y, line in enumerate(lines):
            for i in range(len(direction)):
                for x, letter in enumerate(line):
                    if rec(x, y, 0, i):
                        res += 1
        
        print(res)

    def part2():
        ms = [
            ['M','M'],
            ['S','S']
        ]

        def rotate_2x2(arr: list[list[str]]):
            return [
                [arr[0][1],arr[1][1]],
                [arr[0][0],arr[1][0]]
            ] 

        def check_is_ms(arr: list[list[str]]):
            for _ in range(4):
                if arr == ms:
                    return True
                arr = rotate_2x2(arr)
            return False

        def get_x_ms(x: int, y: int):
            if (x <= 0 or x >= len(lines[0]) - 1 or y <= 0 or y >= len(lines) - 1):
                return None
            return [
                [lines[y-1][x-1],lines[y-1][x+1]],
                [lines[y+1][x-1],lines[y+1][x+1]]
            ]

        res = 0
        for y, line in enumerate(lines):
            for x, letter in enumerate(line):
                if letter == 'A':
                    a_ms = get_x_ms(x, y)
                    if a_ms and check_is_ms(a_ms):
                        res += 1

        print(res)
        # Answ1: 1490 -- too low
        # Answ2: 1972 -- correct! (missed 1 rotation on l58 cause thought it would be covered but nope lol)

    part1()
    part2()

if __name__ == '__main__':
    solution()
