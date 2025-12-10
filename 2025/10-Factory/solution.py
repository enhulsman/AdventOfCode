from z3 import *

def solution():
    file = open("input copy.txt", "r")
    line = file.readline().strip()

    ilds: list[str] = []
    buttons: list[list[list[int]]] = []
    joltage_requirements: list[list[int]] = []

    while line:
        line = line.split(' ')
        ilds.append(line[0].strip('[]'))
        buttons.append( [ [int(num) for num in x.strip('()').split(',')] for x in line[1:-1] ] )
        joltage_requirements.append([int(num) for num in line[-1].strip('{}').split(',')])
        line = file.readline().strip()

    # print(f"{buttons}\n{joltage_requirements}")

    def part1():
        bin_ilds: list[int] = []
        
        def ild_to_binary(ild: str):
            res = 0b0
            for i, c in enumerate(ild):
                if c == '#':
                    res = res | 0b1 << i
            # print(f"{res:0b} <- {ild}")
            return res
        
        def btn_to_binary(btn: list[int]):
            res = 0b0
            for i in btn:
                res = res | 0b1 << i
            # print(f"{res:0b} <- {btn}")
            return res

        def press_btn(ild: int, btn: int):
            # print(f"{ild:0b} ^ {btn:0b} = {ild^btn:0b}")
            return ild ^ btn

        for ild in ilds:
            bin_ilds.append(ild_to_binary(ild))

        def rec(ild: int, btns: list[list[int]], idx: int, num_presses: int, presses: list[int]) -> tuple[bool, int]:
            if ild == 0:
                # print(f"FOUND {idx} - {ild:0b} {num_presses}")
                return (True, num_presses)
            
            if idx >= len(btns):
                # print(f"OOR {idx} - {ild:0b} {presses}")
                return (False, -1)

            btn = btn_to_binary(btns[idx])
            yes, presses_yes = rec(press_btn(ild, btn), btns, idx+1, num_presses+1, presses + [idx])
            no, presses_no = rec(ild, btns, idx+1, num_presses, presses)
            # print(idx, yes, presses_yes, no, presses_no, presses)
            if yes and no:
                return (yes, presses_yes) if presses_yes <= presses_no else (no, presses_no)
            return (yes, presses_yes) if yes else (no, presses_no)

        res = 0
        for i, btns in enumerate(buttons):
            # print(ilds[i], buttons[i])
            succeeded, presses = rec(bin_ilds[i], btns, 0, 0, [])
            if not succeeded:
                print(f"{i} FAILED with {presses}")
            else:
                print(f"{i} Succeeded with {presses}")
                res += presses
        
        print(res)
        return res


    def part2():
        for i, btns in enumerate(buttons):
            amt_btns = len(btns)
            jrqs = joltage_requirements[i]
            btns_pressed = [Int(f'btn_{i}') for i in range(amt_btns)]
            jrq_impacted_by = [[] for _ in range(len(jrqs))]
            for i, btn in enumerate(btns):
                for idx in btn:
                    jrq_impacted_by[idx].append(i)
                
            btns_constraints = []
            for jrq_impact in jrq_impacted_by:
                print(f"{jrq_impact=}")
                # opt.add(Sum([]))

            # total_jrq = 

            print(jrqs, btns)

            opt = Optimize()

            if opt.check() == sat:
                model = opt.model()

        # print(res)
        # return res

    # part1()
    part2()

if __name__ == '__main__':
    solution()
