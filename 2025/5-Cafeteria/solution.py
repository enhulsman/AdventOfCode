def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    ranges: list[tuple[int, int]] = []
    ingredient_ids: list[int] = []

    put_ranges = True
    while line or put_ranges:
        if len(line) < 2:
            put_ranges = False
        elif (put_ranges):
            range = line.split('-')
            ranges.append((int(range[0]),int(range[1])))
        else:
            ingredient_ids.append(int(line))

        line = file.readline().strip()

    ranges.sort()
    ingredient_ids.sort()

    def in_range(range: tuple[int, int], iid: int):
        return iid >= range[0] and iid <= range[1]

    def part1():
        res = 0
        for iid in ingredient_ids:
            for range in ranges:
                if in_range(range, iid):
                    res += 1
                    break
        
        print(res)

    def range_len(range: tuple[int, int]):
        return (range[1] - range[0]) + 1

    def part2():
        res = 0
        for idx, range in enumerate(ranges):
            if  idx > 0 and range[0] <= ranges[idx-1][1]:
                if ranges[idx-1][1] >= range[1]:
                    # print("Invalid new range, already covered, skipping")
                    continue
                ranges[idx] = (ranges[idx-1][1] + 1, range[1])
            # print(idx, range, ranges[idx], range != ranges[idx])
            res += range_len(ranges[idx])
        print(res)

        # Answ1: 436164823559766 -- too high
        # Answ2: 342291610519606 -- too low
        # Answ3: 353507173555373 -- correct!

    part1()
    part2()

if __name__ == '__main__':
    solution()
