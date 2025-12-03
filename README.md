# Advent of Code

My solutions for Advent of Code challenges across multiple years.

## Structure

```text
AdventOfCode/
├── 2024/           # Advent of Code 2024 solutions
│   ├── 1-HistorianHysteria/
│   └── ...
├── 2025/           # Advent of Code 2025 solutions
│   ├── 1-SecretEntrance/
│   ├── 2-GiftShop/
│   └── ...
└── 20XX/           # Future years...
```

## Getting Started

### Creating a New Problem

Use the `new_problem.py` script to automatically create a new problem directory with the template files.

**Automatic mode** (fetches problem name from Advent of Code):
```bash
python3 new_problem.py <year> <day>
```

**Manual mode** (specify problem name yourself):
```bash
python3 new_problem.py <year> <day> <problem_name>
```

**Examples:**
```bash
# Automatic - fetches "Red-Nosed Reports" and creates "2-RedNosedReports"
python3 new_problem.py 2024 2

# Manual - specify the name yourself
python3 new_problem.py 2024 3 TobogganTrajectory
```

This will create:
- `{year}/{day}-{ProblemName}/` directory
- `solution.py` with the starter template
- Empty `input.txt` for your puzzle input

### Workflow

1. Create a new problem directory: `python3 new_problem.py 2024 3`
2. Copy your puzzle input from Advent of Code to `input.txt`
3. Implement `part1()` and `part2()` in `solution.py`
4. Run your solution: `python3 solution.py`

## Years

- [2024](./2024/) - Previous year
- [2025](./2025/) - Current year
