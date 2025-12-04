def solution():
    import re
    file = open("input.txt", "r")
    line = file.readline().strip()

    lines: str = ""

    while line:
        lines += line
        line = file.readline().strip()

    def part1():
        res = 0
        operands_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        multiplications: list[tuple[str, str]] = re.findall(operands_pattern, lines)
        for x, y in multiplications:
            res += int(x) * int(y)

        print(res)


    def part2():
        res = 0
        enabled_ops_pattern = r'(.+?)(?:don\'t\(\)).+?(?:do\(\))' # Doesn't capture text after final 'do()'
        enabled_ops_pattern = r'.+?(?:do\(\))(.+?)(?:don\'t\(\))' # Doesn't capture text before first 'do()'
        # 1-liner? - r'(?s)(?<!don't\(\))(?:mul\((\d{1,3}),(\d{1,3})\))+.*?(?=do\(\))'
        operands_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        matches = re.findall(enabled_ops_pattern, lines)
        for match in matches:
            multiplications: list[tuple[str, str]] = re.findall(operands_pattern, match)
            print(match, multiplications)
            for x, y in multiplications:
                res += int(x) * int(y)


        print(res)

    part1()
    part2()

if __name__ == '__main__':
    solution()
