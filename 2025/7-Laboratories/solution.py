def solution():
    file = open("/Users/ix45uu/Developer/AdventOfCode/2025/7-Laboratories/input.txt", "r")
    line = file.readline().strip()

    lines: list[list[str]] = []

    while line:
        lines.append([x for x in line])
        line = file.readline().strip()
    
    global split_total
    split_total = 0

    def rec1(x: int, y: int, split: int):
        global split_total
        if y >= len(lines):
            return split
        print(x,y,lines[y][x])
        if lines[y][x] == '^':
            split_total += 1
            return rec1(x-1, y, 1) + rec1(x+1, y, split+1)
        if lines[y][x] == '|':
            return split - 1
        if lines[y][x] == '.':
            lines[y][x] = '|'
            return rec1(x,y+1,split)
        else: 
            print(f"shouldn't exist!?! - {x=} {y=}, {lines[y][x]}, {split}")
    
    def part1():
        start = lines[0].index('S')
        print(start, lines[1][start])
        print(rec1(start, 1, 1))
        print(split_total)
        # Answ1: 68696 -- too high

    def part2():
        from functools import lru_cache
        @lru_cache(maxsize=10000)
        def rec(x: int, y: int):
            if y >= len(lines):
                print(f"Finished at {x=}, {y=}")
                return 1
            print(x,y,lines[y][x])
            if lines[y][x] == '^':
                return (rec(x-1, y) + rec(x+1, y))
            # if lines[y][x] == '|':
            #     return 0
            if lines[y][x] == '.':
                # lines[y][x] = '|'
                return rec(x,y+1)
            else: 
                print(f"shouldn't exist!?! - {x=} {y=}, {lines[y][x]}")
                return -1
        
        start = lines[0].index('S')
        print(start, lines[1][start])
        print(rec(start, 1))
        
    # part1()
    part2()   

if __name__ == '__main__':
    solution()
