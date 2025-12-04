def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    lines: list[list[str]] = []

    print([x for x in line])

    while line:
        lines.append([x for x in line])
        line = file.readline().strip()

    def check_surrounding(row: int, col: int) -> int:
        idxs = [
            (col-1, row-1),(col, row-1),(col+1, row-1),
            (col-1, row),               (col+1, row),
            (col-1,row+1), (col,row+1), (col+1, row+1)
        ]

        count = 0
        for c, r in idxs:
            if (r < 0 or c < 0 or r >= 140 or c >= 140)  or lines[r][c] != '@':
                continue
            count += 1
        
        return count


    def part1():
        res = 0
        for row, line in enumerate(lines):
            for col, roll in enumerate(line):
                if roll == '.':
                    continue
                if check_surrounding(row, col) < 4:
                    res += 1
        
        print(res)
            
    def part2():
        res = 0
        removed = -1
        def remove_roll(row: int, col: int):
            lines[row][col] = '.'
        
        while removed != 0:
            removed = 0
            to_remove: list[tuple[int, int]] = []
            for row, line in enumerate(lines):
                for col, roll in enumerate(line):
                    if roll == '.':
                        continue
                    if check_surrounding(row, col) < 4:
                        to_remove.append((row,col))

            for row, col in to_remove:
                remove_roll(row, col)
                removed += 1

            res += removed

        print(res)
            

    part1()
    part2()

if __name__ == '__main__':
    solution()
