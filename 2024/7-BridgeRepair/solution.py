def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    equations: list[tuple[int, list[int]]] = []

    while line:
        split = line.split(':')
        equations.append((int(split[0]), [int(x) for x in split[1].strip().split(' ')]))
        line = file.readline().strip()

    def part1():
        def rec(evaluation: int, numbers: list[int], result: int) -> bool:
            # print(evaluation, numbers, res)
            if not numbers:
                return result == evaluation

            plus = rec(evaluation, numbers[1:], result+numbers[0])
            mult = rec(evaluation, numbers[1:], result*numbers[0])

            return plus or mult
        
        res = 0
        for evaluation, numbers in equations:
            if rec(evaluation, numbers[1:], numbers[0]):
                res += evaluation
        
        print(res)

    def part2():
        def rec(evaluation: int, numbers: list[int], result: int) -> bool:
            # print(evaluation, numbers, res)
            if not numbers:
                return result == evaluation

            plus = rec(evaluation, numbers[1:], result+numbers[0])
            mult = rec(evaluation, numbers[1:], result*numbers[0])
            concat = rec(evaluation, numbers[1:], int(str(result) + str(numbers[0])))

            return plus or mult or concat
        
        res = 0
        for evaluation, numbers in equations:
            if rec(evaluation, numbers[1:], numbers[0]):
                res += evaluation
        
        print(res)

    part1()
    part2()

if __name__ == '__main__':
    solution()
