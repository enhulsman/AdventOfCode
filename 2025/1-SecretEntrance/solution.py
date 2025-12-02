def move_dial(line: str, dial: int) -> int:
    dir = line[0]
    num = line[1:]
    
    return dial + int(num) if dir == "R" else dial - int(num)

def solution_part1():
    file = open("input.txt", "r")
    line = file.readline().strip()

    dial = 50
    count = 0

    while line:
        dial = move_dial(line, dial)
        while dial > 99:
            dial -= 100
        
        while dial < 0:
            dial += 100
        
        if dial == 0:
            count += 1

        line = file.readline().strip()
    file.close()

    print(f"Password is: {count}")

def solution_part2():
    file = open("input.txt", "r")
    line = file.readline().strip()

    dial = 50
    count = 0
    was_zero = False

    while line:
        dial = move_dial(line, dial)
        while dial > 99:
            count += 1
            dial -= 100
        
        while dial < 0:
            if not was_zero: 
                count += 1
            dial += 100
        
        was_zero = False
        if dial == 0:
            count += 1
            was_zero = True

        line = file.readline().strip()
    file.close()

    print(f"Password is: {count}")

if __name__ == '__main__':
    solution_part1()
    solution_part2()