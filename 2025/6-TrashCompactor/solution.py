def solution():
    file = open("/Users/ix45uu/Developer/AdventOfCode/2025/6-TrashCompactor/input.txt", "r")
    line = file.readline()

    ops: list[str] = []
    ops_matrixes: list[list[list[str]]] = []

    while line:
        ops.append(line)
        line = file.readline()

    operators = ops[len(ops) - 1].split()

    def extract_ops_matrix(ops: list[str]):
        matrix_width = 0
        for i, c in enumerate(ops[len(ops)-1]):
            is_last = i == len(ops[0]) - 1
            if c != ' ' or is_last:
                if i == 0: continue
                if is_last: 
                    matrix_width += 1
                    i += 1
                start_idx = i - matrix_width

                op_matrix: list[list[str]] = []
                for row in ops[:-1]:
                    op_matrix.append([x for x in row[start_idx-1:start_idx+matrix_width-1]])

                # print(f"{start_idx} - {matrix_width} - {op_matrix=}")
                ops_matrixes.append(op_matrix)

                matrix_width = 0
            else:
                matrix_width += 1
    
    extract_ops_matrix(ops)

    def part1():
        part2(False)

    def part2(rotate: bool = True):
        import numpy as np
        res = 0
        for i, ops_matrix in enumerate(ops_matrixes):
            np_ints = np.array(ops_matrix)
            rotated_ops = np.rot90(np_ints)
            arr_to_use = rotated_ops if rotate else ops_matrix
            op = operators[i]
            flat_ints = [''.join(x) for x in arr_to_use]
            result = eval(op.join(flat_ints))
            # print(result)
            res += result
        
        print(res)

    part1()
    part2()

if __name__ == '__main__':
    solution()
