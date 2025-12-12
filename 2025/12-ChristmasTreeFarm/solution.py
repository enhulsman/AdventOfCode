import re

def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    shapes_str: list[list[list[str]]] = []
    shapes: list[list[tuple[int, int]]] = []
    grids: list[tuple[int,int,list[int]]] = []

    skip_empty_lines = True
    shape = 0
    while line or skip_empty_lines:
        if re.match(r'^\d:$', line):
            shape = int(line[0])
        elif re.match(r'\d+x\d+:', line):
            skip_empty_lines = False
            split = line.split(':')
            size = split[0].split('x')
            x = int(size[0])
            y = int(size[1])
            grids.append((x,y,[int(c) for c in split[1].strip().split()]))
        else:
            if len(shapes_str) == shape:
                shapes_str.append([[c for c in line]])
            elif line:
                shapes_str[shape].append([c for c in line])

        line = file.readline().strip()
    
    for shape in shapes_str:
        res: list[tuple[int, int]] = []
        for y, line in enumerate(shape):
            for x, char in enumerate(line):
                if char == '#':
                    res.append((x-1, y-1))
        shapes.append(res)

    def rotate_shape(shape: list[tuple[int, int]]):
        rotated_shape = []
        for x, y in shape:
            rotated_shape.append((y, -x))
        return rotated_shape
    
    def count_wb_shape(shape: list[tuple[int, int]]):
        w = 0
        b = 0
        for x, y in shape:
            if abs(x + y) % 2 == 0: w += 1
            else:                   b += 1
        return (w, b)

    def count_wb_grid(x: int, y: int):
        size = x * y
        return (size - size // 2, size // 2)

    def parity_signature(t: tuple[int, int]):
        return t[0] - t[1]

    for shape in shapes:
        print(shape, count_wb_shape(shape))
        print(rotate_shape(shape), count_wb_shape(rotate_shape(shape)))


    def part1():
        grid: set[tuple[int, int]] = set()
        res = 0
        for max_x, max_y, shape_counts in grids:
            grid_size = max_x * max_y
            total_parity_signature = 0
            total_size = 0
            for i, shape in enumerate(shapes):
                shape_w, shape_b = count_wb_shape(shape)
                shape_size = shape_w + shape_b
                even = shape_counts[i] % 2 == 0
                shape_parity_signature = parity_signature((shape_w, shape_b)) if not even else 0
                if total_parity_signature <= 0: 
                    total_parity_signature += shape_parity_signature
                else:
                    total_parity_signature -= shape_parity_signature
                total_shape_size = shape_counts[i] * shape_size
                total_size += total_shape_size
            
            if total_size + abs(total_parity_signature) <= grid_size:
                res += 1
        
        print(res)
        return res

    def part2():
        print("WE MADE IT!!!!")

    part1()
    part2()

if __name__ == '__main__':
    solution()
