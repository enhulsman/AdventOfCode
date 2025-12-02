def solution_part1():
    file = open("input.txt", "r")
    lines = file.readline().strip().split(",")

    res = 0

    for line in lines:
        start = int(line.split("-")[0])
        end = int(line.split("-")[1])
        for i in range(start, end + 1):
            i_string = str(i)
            len_i_string = len(i_string)
            if len_i_string % 2 != 0:
                continue
            middle = len_i_string // 2
            op_a = int(i_string[:middle])
            op_b = int(i_string[middle:])
            if (op_a == op_b):
                # print (op_a, op_b)
                res += i

    print(res)
    return res

def solution_part2():
    file = open("input.txt", "r")
    lines = file.readline().strip().split(",")

    res = 0

    for line in lines:
        start = int(line.split("-")[0])
        end = int(line.split("-")[1])
        for i in range(start, end + 1):
            i_string = str(i)
            len_i_string = len(i_string)
            for j in range(1, (len_i_string // 2) + 1):
                if len_i_string % j != 0:
                    continue
                else:
                    id_slice = i_string[:j]
                    reconstructed = id_slice * (len_i_string // j)
                    if (reconstructed == i_string):
                        # print (id_slice, i_string)
                        res += i
                        break

    print(res)
    return res


if __name__ == '__main__':
    solution_part1()
    solution_part2()