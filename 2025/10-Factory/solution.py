from string import ascii_lowercase
from functools import lru_cache
import sys

# sys.setrecursionlimit(10000)

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

    print(f"{buttons}\n{joltage_requirements}")

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
        def press_btn(jrq: list[int], btn: list[int]) -> list[int]:
            for i in btn:
                jrq[i] -= 1
            return jrq
        
        def list_to_b400(num_list: list[int]) -> str:
            # base 400 works as two ints of base 20
            # base 20 works from 0-9 a-j
            res = ""
            for num in num_list:
                byte = [num // 20, num % 20]
                b400 = ""
                for n in byte:
                    # print("LIST->B400", num_list, byte, n)
                    b400 += str(ascii_lowercase[n-10]) if n > 9 else str(n)

                res += f"{b400}"
            # print(res)
            return res
        
        def b400_to_list(num: str) -> list[int]:
            res = []
            for i in range(0, len(num), 2):
                res.append(int(num[i:i+2], base=20))
            # print("B400->LIST", num, res)
            return res 
        
        def list_list_to_b400_arr(btns: list[list[int]]) -> str:
            return ','.join(list_to_b400(x) for x in btns)

        def b400_arr_to_list_list(b400_arr: str) -> list[list[int]]:
            res = []
            for b400 in b400_arr.split(","):
                res.append(b400_to_list(b400))
            return res

        @lru_cache(maxsize=10000)
        def rec(jrq_b400: str, btns_b400_arr: str, idx: int, num_presses: int, presses_b400: str) -> tuple[bool, int]:
            jrq = b400_to_list(jrq_b400)
            btns = b400_arr_to_list_list(btns_b400_arr)
            presses = b400_to_list(presses_b400)

            if jrq.count(0) == len(jrq):
                # print(f"FOUND {idx} - {ild:0b} {num_presses}")
                return (True, num_presses)
            
            if idx >= len(btns):
                # print(f"OOR {idx} - {ild:0b} {presses}")
                return (False, -1)

            btn = btns[idx]
            yes, presses_yes = rec(list_to_b400(press_btn(jrq, btn)), list_list_to_b400_arr(btns), idx, num_presses+1, list_to_b400(presses + [idx]))
            no, presses_no = rec(list_to_b400(jrq), list_list_to_b400_arr(btns), idx+1, num_presses, list_to_b400(presses))
            # print(idx, yes, presses_yes, no, presses_no, presses)
            if yes and no:
                return (yes, presses_yes) if presses_yes <= presses_no else (no, presses_no)
            return (yes, presses_yes) if yes else (no, presses_no)

        res = 0
        for i, btns in enumerate(buttons):
            print(joltage_requirements[i], btns)

            succeeded, presses = rec(list_to_b400(joltage_requirements[i]), list_list_to_b400_arr(btns), 0, 0, list_to_b400([]))
            if not succeeded:
                print(f"{i} FAILED with {presses}")
            else:
                print(f"{i} Succeeded with {presses}")
                res += presses
        
        print(res)
        return res

    # part1()
    part2()

if __name__ == '__main__':
    solution()
