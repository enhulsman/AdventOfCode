def move_dial(line: bytes, dial: int) -> int:
    dir = line[0]
    num = line[1:]
    
    return dial + int(num) if dir == "R" else dial - int(num)

def solution():
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
        
        # print(dial)
        was_zero = False
        if dial == 0:
            count += 1
            was_zero = True

        line = file.readline().strip()
    file.close()

    print(f"Password is: {count}")


if __name__ == '__main__':
    solution()