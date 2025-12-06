def solution():
    file = open("/Users/ix45uu/Developer/AdventOfCode/2024/5-PrintQueue/input.txt", "r")
    line = file.readline().strip()

    rules: dict[int, list[int]] = {}
    updates: list[list[int]] = []
    invalid_updates: list[tuple[tuple[int, int], list[int]]] = []

    put_rules = True
    while line or put_rules:
        if len(line) < 2:
            put_rules = False
        elif (put_rules):
            xy = line.split("|")
            x = int(xy[0])
            y = int(xy[1])
            if not rules.get(y):
                rules[y] = [x]
            else:
                rules[y].append(x)
        else:
            updates.append([int(x) for x in line.split(",")])

        line = file.readline().strip()


    def check_page_satisfies_rules(update: list[int], idx: int, page: int) -> int:
        for rule in rules[page]:
            if update[idx+1:].count(rule) > 0:
                # print(f"{page} cannot come before {rule} - {update} - {rules[page]}\n")
                return rule
        return 0

    def check_valid_update(update: list[int], append: bool = True) -> int:
        for idx, page in enumerate(update):
            invalid_rule = check_page_satisfies_rules(update, idx, page)
            if invalid_rule > 0:
                if append:
                    # print(f"{idx} - {page} - {update}\n{rules[page]}\n")
                    invalid_updates.append(((idx, update.index(invalid_rule)), update))
                return 0
        else:
            return update[len(update) - (len(update) // 2) - 1]

    def part1():
        res = 0
        for update in updates:
            res += check_valid_update(update)
        
        print(res)
        # Answ1: 5690 -- too low
        # Answ2: 5732 -- correct!

    def part2():
        res = 0
        
        for (idx, bad_idx), update in invalid_updates:
            update.insert(idx,update.pop(bad_idx))
            fix_res = check_valid_update(update, False)
            if fix_res > 0: print("Fixed")
            res += fix_res

        print(res)

    part1()
    part2()

if __name__ == '__main__':
    solution()
