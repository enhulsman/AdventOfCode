def solution():
    file = open("/Users/ix45uu/Developer/AdventOfCode/2025/8-Playground/input.txt", "r")
    line = file.readline().strip()

    junction_boxes: list[list[int]] = []
    
    while line:
        junction_boxes.append([int(x) for x in line.split(',')])
        line = file.readline().strip()

    def distance(p: list[int], q: list[int]) -> float:
        import math
        if len(p) < 3 or len(q) < 3: return -1
        return math.sqrt(((p[0] - q[0])**2) + ((p[1] - q[1])**2) + ((p[2] - q[2])**2))


    distances: list[tuple[float, int, int]] = []
    for i, box in enumerate(junction_boxes):
        for j, box2 in enumerate(junction_boxes[i+1:], start=i+1):
            distances.append( (distance(box, box2), i, j) )

    distances = sorted(distances)

    def part1():
        MAX_PAIRS = 10 if len(junction_boxes) < 100 else 1000
        circuits: list[list[int]] = []

        # print(distances)
        connections_made = 0
        for i, curr_distance in enumerate(distances):
            if connections_made == MAX_PAIRS:
                break
            # print(curr_distance[0], end='\t - ')
            box1 = curr_distance[1]
            box2 = curr_distance[2]
            # print(box1, box2, junction_boxes[box1], junction_boxes[box2], end= ' - \t')
            
            box1_circuits = []
            box2_circuits = []

            for i, circuit in enumerate(circuits):
                if circuit.count(box1):
                    box1_circuits.append(i)
                if circuit.count(box2):
                    box2_circuits.append(i)
            
            if not box1_circuits and not box2_circuits:
                circuits.append([box1, box2])
                connections_made += 1
                # print(f"Added {box1} and {box2} to new group - {connections_made}")
            elif box1_circuits and box2_circuits:
                if box1_circuits[0] == box2_circuits[0]:
                    connections_made += 1
                    # print(f"BOX1&BOX2 equal {box1_circuits=} {box2_circuits=}")
                    continue
                # print(f"Merging {circuits[box1_circuits[0]]} and {circuits[box2_circuits[0]]}")
                for box in circuits[box2_circuits[0]]:
                    circuits[box1_circuits[0]].append(box)
                circuits.remove(circuits[box2_circuits[0]])
                connections_made += 1
            elif box1_circuits:
                # print(box1_circuits, len(circuits))
                circuits[box1_circuits[0]].append(box2)
                connections_made += 1
                # print(f"Added {box2} to {circuits[box1_circuits[0]]} - {connections_made}")
            elif box2_circuits:
                circuits[box2_circuits[0]].append(box1)
                connections_made += 1
                # print(f"Added {box1} to {circuits[box2_circuits[0]]} - {connections_made}")
            # else:
                # print(f"\n\n\n\n WTF HAPPENED? {box1_circuits=} {box2_circuits=} {circuits=} {box1=} {box2=} \n\n\n\n")

        circuit_lens: list[int] = sorted([len(circuit) for circuit in circuits], reverse=True)
        # print(circuit_lens)
        # print(circuits)
        return circuit_lens[0] * circuit_lens[1] * circuit_lens[2]
        # Answ1: 102856 -- too low
        # Answ2: 14400 -- too low
        # Answ3: 175500 -- correct!


    def part2():
        circuits: list[list[int]] = []
        connections_made = 0
        last_boxes = (-1,-1)
        for i, curr_distance in enumerate(distances):
            if len(circuits) > 0 and len(circuits[0]) == len(junction_boxes):
                break
            # print(curr_distance[0], end='\t - ')
            box1 = curr_distance[1]
            box2 = curr_distance[2]
            last_boxes = (box1, box2)
            # print(box1, box2, junction_boxes[box1], junction_boxes[box2], end= ' - \t')
            
            box1_circuits = []
            box2_circuits = []

            for i, circuit in enumerate(circuits):
                if circuit.count(box1):
                    box1_circuits.append(i)
                if circuit.count(box2):
                    box2_circuits.append(i)
            
            if not box1_circuits and not box2_circuits:
                circuits.append([box1, box2])
                connections_made += 1
                # print(f"Added {box1} and {box2} to new group - {connections_made}")
            elif box1_circuits and box2_circuits:
                if box1_circuits[0] == box2_circuits[0]:
                    connections_made += 1
                    # print(f"BOX1 & BOX2 in same circuit {box1_circuits=} {box2_circuits=} - {connections_made}")
                    continue
                # print(f"Merging {circuits[box1_circuits[0]]} and {circuits[box2_circuits[0]]}")
                for box in circuits[box2_circuits[0]]:
                    circuits[box1_circuits[0]].append(box)
                circuits.remove(circuits[box2_circuits[0]])
                connections_made += 1
            elif box1_circuits:
                circuits[box1_circuits[0]].append(box2)
                connections_made += 1
                # print(f"Added {box2} to {circuits[box1_circuits[0]]} - {connections_made}")
            elif box2_circuits:
                circuits[box2_circuits[0]].append(box1)
                connections_made += 1
                # print(f"Added {box1} to {circuits[box2_circuits[0]]} - {connections_made}")
            # else:
                # print(f"\n\n\n\n WTF HAPPENED? {box1_circuits=} {box2_circuits=} {circuits=} {box1=} {box2=} \n\n\n\n")

        # print(sorted(circuits[0]))
        # print(last_boxes)
        return junction_boxes[last_boxes[0]][0] * junction_boxes[last_boxes[1]][0]
        # Answ1: 6093282 -- too low
        # Answ2: 6934702555 -- correct!

    print(part1())
    print(part2())

if __name__ == '__main__':
    solution()
