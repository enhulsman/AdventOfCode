def solution():
    file = open("input.txt", "r")
    line = file.readline().strip()

    device_outputs: dict[str, list[str]] = {}
    outputs_in: dict[str, list[str]] = {}

    while line:
        line = line.split(':')
        origin = line[0]
        outputs = line[1].strip().split(' ')
        device_outputs[origin] = [x for x in outputs]
        for op in outputs:
            if outputs_in.get(op):
                outputs_in[op].append(origin)
            else:
                outputs_in[op] = [origin]
        line = file.readline().strip()
    
    for op in outputs_in:
        for origin in outputs_in[op]:
            assert(op in device_outputs[origin])

    def part1():
        from functools import lru_cache
        @lru_cache(maxsize=10000)
        def rec(output: str, passed: frozenset[str]):
            if output == 'out':
                return 1
            
            if not device_outputs.get(output):
                return 0

            res = 0
            for device in device_outputs[output]:
                if device not in passed:
                    new_set = passed | {device}
                    res += rec(device, new_set)             

            return res
        
        res = rec('you', frozenset())
        print(res)
        return res

    def part2():
        from functools import lru_cache
        dac_fft = ['dac', 'fft']

        @lru_cache(maxsize=10000)
        def backwards_rec(output: str, passed: frozenset[str]):
            if output == 'svr':
                return 1 if all(x in passed for x in dac_fft) else 0

            if not outputs_in.get(output):
                return 0

            res = 0
            for device in outputs_in[output]:
                updated_passed = passed | {output} if output in dac_fft else passed
                res += backwards_rec(device, updated_passed)

            return res
        
        res = 0
        res = backwards_rec('out', frozenset())
        print(res)
        return res

    part1()
    part2()

if __name__ == '__main__':
    solution()
