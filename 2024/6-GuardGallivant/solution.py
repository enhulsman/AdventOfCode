def solution():
    file = open("/Users/ix45uu/Developer/AdventOfCode/2024/6-GuardGallivant/input.txt", "r")
    line = file.readline().strip()

    path_map: list[list[str]] = []

    while line:
        path_map.append([x for x in line])
        line = file.readline().strip()

    from enum import Enum
    class Direction(Enum):
        UP = (0, -1)
        RIGHT = (1, 0)
        DOWN = (0, 1)
        LEFT = (-1, 0)

        def rotate(self):
            match self:
                case Direction.UP:
                    return Direction.RIGHT
                case Direction.RIGHT:
                    return Direction.DOWN
                case Direction.DOWN:
                    return Direction.LEFT
                case Direction.LEFT:
                    return Direction.UP

    
    def add_dir(pos: tuple[int, int], dir: Direction) -> tuple[int, int]:
        return (pos[0] + dir.value[0], pos[1] + dir.value[1])

    def is_outside_map(x: int, y: int):
        return x < 0 or x > len(path_map[0]) or y < 0 or y > len(path_map)

    def part1(part2: bool = False):
        points_crossed = 1
        cross_points = 0
        curr_dir = Direction.UP
        guard_x, guard_y = (-1, -1)
        for y, line in enumerate(path_map):
            if line.count('^') > 0:
                guard_x, guard_y = (line.index('^'), y)

        
        while not is_outside_map(guard_x, guard_y):
            new_x, new_y = add_dir((guard_x,guard_y), curr_dir)
            
            if path_map[guard_y][guard_x] == 'X':
                cross_points += 1
            else:
                print(guard_x, guard_y, path_map[guard_y][guard_x], path_map[new_y][new_x])
            
            if path_map[guard_y][guard_x] == '.':
                path_map[guard_y][guard_x] = 'X'
                points_crossed += 1
            
            while path_map[new_y][new_x] == '#':
                curr_dir = curr_dir.rotate()
                new_x, new_y = add_dir((guard_x,guard_y), curr_dir)
                # print(f"rotate at ({guard_x},{guard_y}) to {curr_dir}")
            
            guard_x, guard_y = new_x, new_y
        
        return points_crossed if not part2 else cross_points

    def part2():
        return part1(True)
        # Answ2: 490 -- too low

    # print(part1())
    print(part2())

if __name__ == '__main__':
    solution()
