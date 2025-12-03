def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    all_joltages: list[str] = []
    while line:
        all_joltages.append(line)
        line = file.readline().strip()


    def part1(): # Ngl, ugly af
        def find_largest_num(jolt: str) -> int:
            max_num = 0
            val = 0
            edge_case_num = -1
            for i in reversed(range(1,10)):
                count_i = jolt.count(str(i))
                if count_i > 1:
                    val = int(str(i) * 2)
                if count_i > 0:
                    if jolt.find(str(i)) == 99:
                        print(f"EDGE CASE:\n{jolt=}\n{i=}, {count_i=}, {jolt.find(str(i))=}")
                        edge_case_num = i
                    else:
                        max_num = i
                        break
            if edge_case_num >= 0: 
                print(f"{max_num=}, {val=}, {edge_case_num=}, {int(str(max_num)+str(edge_case_num))=}")
                return int(str(max_num)+str(edge_case_num))
            return max(max_num, val)
        
        joltages = all_joltages
        res = 0
        for jolt in joltages:
            max_num = find_largest_num(jolt)
            # if edge_case: print(f"{jolt=}\n{max_num=}")
            if max_num > 9:
                res += max_num
                continue
            idx = jolt.find(str(max_num))
            max_num2 = find_largest_num(jolt[idx+1:])
            joltage = int(str(max_num)+str(max_num2)[0])
            # if edge_case: print(f"{idx=}\n{max_num2=}\n{joltage=}")
            # print(joltage)
            res += joltage
            
        print(res)
        # Answ1: 16951 -- too high
        # Answ2: 16908 -- too low
        # Answ3: 16945 -- too low !?!?!?!?!
        # Answ4: 16946 -- correct!

    def find_all_idx(jolt: str, num: int) -> list[int]:
        res = []
        next_num = jolt.find(str(num))
        while next_num >= 0:
            res.append(next_num)
            next_num = jolt.find(str(num), next_num+1)

        return res

    def part2():
        joltages = all_joltages
        res = 0
        MAX_LEN = 12
        for jolt in joltages:
            jolt_dict: dict[int, list[int]] = {}
            for i in reversed(range(1,10)):
                jolt_dict[i] = find_all_idx(jolt, i)
            
            print(jolt)
            print(jolt_dict)
            
            max_num: list[int] = []
            while len(max_num) < 12:
                for i in reversed(range(1,10)):
                    idxs = jolt_dict.get(i)
                    exclude_idx_greater_than = MAX_LEN - len(max_num)
                    if not idxs: continue
                    
                    for idx in idxs:
                        if (not max_num or idx > max_num[-1]) and len(jolt) - idx >= exclude_idx_greater_than:
                            max_num.append(idx)
                            print(f"Added {idx} to {max_num}")
                            # idxs.remove(idx)
                            # jolt_dict[i] = idxs
                            break
                    else:
                        continue
                    break
                        # if (not max_num or idx > max_num[-1]) and 100 - idx > MAX_LEN - len(max_num) and len(max_num) < MAX_LEN:
                        #     max_num.append(idx)
                
                        # if max_num and 100 - max_num[-1] == MAX_LEN - len(max_num):
                        #     for i in range(max_num[-1]+1, 100):
                        #         max_num.append(i)

            print(max_num)

            joltage = ""
            for idx in max_num:
                joltage += jolt[idx]
            
            print(joltage)

            res += int(joltage)
        
        print(res)
        # Answ1: 168423560532785 -- too low
        # Answ2: 168627047606506 -- correct!

    # part1()
    part2()

if __name__ == '__main__':
    solution()