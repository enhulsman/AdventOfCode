def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    antennas: dict[str, list[tuple[int, int]]] = {}
    grid_width = len(line)

    y = 0
    while line:
        for x, c in enumerate(line):
            if c != '.':
                if not antennas.get(c):
                    antennas[c] = [(x, y)]
                else:
                    antennas[c].append((x, y))
        y += 1
        line = file.readline().strip()
    
    grid_height = y
    print(antennas, grid_width, grid_height)

    def subtract_vectors(p1: tuple[int, int], p2: tuple[int, int]):
        return (p1[0] - p2[0], p1[1] - p2[1])

    def add_vectors(p1: tuple[int, int], p2: tuple[int, int]):
        return (p1[0] + p2[0], p1[1] + p2[1])

    def inside_grid(p: tuple[int, int], width: int, height: int):
        return p[0] >= 0 and p[1] >= 0 and p[0] < width and p[1] < height

    """     
    .   .   .   an2 
    .   .   x2  . (2,1)
    .   x1  .   . (1,2)
    an1 .   .   . 

    x1 = (1,2)
    x2 = (2,1)
    dv = (1,2) - (2,1) = (-1,1)
    x1 - dv = (1,2) - (-1,1) = (2,1) = x2
    x1 + dv = (1,2) + (-1,1) = (0,1) = an1
    x2 - dv = (2,1) - (-1,1) = (3,2) = an2

    """

    def part1():
        res = 0
        anti_nodes: set[tuple[int, int]] = set()
        for nodes in antennas.values():
            for i, node in enumerate(nodes):
                if i+1 >= len(nodes): continue
                for next_node in nodes[i+1:]:
                    distance_vector = subtract_vectors(node, next_node)
                    anti = [add_vectors(node, distance_vector), subtract_vectors(next_node, distance_vector)]
                    [anti_nodes.add(an) for an in anti]
        for an in anti_nodes:
            if inside_grid(an, grid_width, grid_height):
                res += 1

        print(res)

    def part2():
        anti_nodes: set[tuple[int, int]] = set()
        
        for nodes in antennas.values():
            for i, node in enumerate(nodes):
                if i+1 >= len(nodes): continue
                for next_node in nodes[i+1:]:
                    [anti_nodes.add(x) for x in [node, next_node]]
                    distance_vector = subtract_vectors(node, next_node)
                    plus_anti = add_vectors(node, distance_vector)
                    while inside_grid(plus_anti, grid_width, grid_height):
                        anti_nodes.add(plus_anti)
                        plus_anti = add_vectors(plus_anti, distance_vector)
                    minus_anti = subtract_vectors(next_node, distance_vector)
                    while inside_grid(minus_anti, grid_width, grid_height):
                        anti_nodes.add(minus_anti)
                        minus_anti = subtract_vectors(minus_anti, distance_vector)

        print(len(anti_nodes))

    part1()
    part2()

if __name__ == '__main__':
    solution()
