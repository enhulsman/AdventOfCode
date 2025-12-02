def solution_part1():
    file = open("input.txt", "r")
    line = file.readline().strip()

    left = []
    right = []

    while line:
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))

        line = file.readline().strip()
    
    left.sort()
    right.sort()

    res = 0

    for i in range(len(left)):
        res += abs(left[i] - right[i])

    print(res)

def solution_part2():
    pass

if __name__ == "__main__":
    solution_part1()
    solution_part2()