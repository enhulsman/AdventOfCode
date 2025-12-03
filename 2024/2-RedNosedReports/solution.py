def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()
    
    reports: list[list[int]] = []

    while line:
        reports.append([int(x) for x in line.split()])
        line = file.readline().strip()

    def check_safe_report(report: list[int], remove_bad_reading: bool = False) -> bool:
        prev_reading = report[0]
        upwards = report[-1] - prev_reading > 0
        for idx, next_reading in enumerate(report[1:]):
            is_correct_direction = (next_reading > prev_reading) if upwards else (next_reading < prev_reading)
            is_safe_change = (next_reading - prev_reading <= 3) if upwards else (prev_reading - next_reading <= 3)
            if is_correct_direction and is_safe_change:
                prev_reading = next_reading
                continue
            else:
                if remove_bad_reading:
                    remove_curr = report.copy()
                    remove_next = report.copy()
                    remove_curr.pop(idx)
                    remove_next.pop(idx + 1)
                    ret1, ret2 = (check_safe_report(remove_curr, False), check_safe_report(remove_next, False))
                    return ret1 or ret2
                else:
                    return False
        return True

    def part1():
        safe = 0
        for report in reports:
            if check_safe_report(report): 
                safe += 1
        print(safe)

    def part2():
        safe = 0
        for report in reports:
            if check_safe_report(report, True):
                safe += 1
        print(safe)

    part1()
    part2()

if __name__ == '__main__':
    solution()