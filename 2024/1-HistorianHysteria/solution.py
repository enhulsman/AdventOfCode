def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    left = []
    right = []

    while line:
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))

        line = file.readline().strip()
    
    def part1():
        left.sort()
        right.sort()

        res = 0

        for i in range(len(left)):
            res += abs(left[i] - right[i])

        print(res)

    def part2():
        dict = {}
        res = 0
        for id in right:
            if not dict.get(id):
                dict[id] = 1
            else:
                dict[id] += 1
        
        for id in left:
            amt = dict.get(id)
            if amt:
                res += id * amt

        print(res)
            
    part1()
    part2()

if __name__ == "__main__":
    solution()