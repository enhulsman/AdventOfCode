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

**Automatic mode** (fetches problem name and input from Advent of Code):
```bash
python3 new_problem.py <year> <day>
```

**Manual mode** (specify problem name yourself):
```bash
python3 new_problem.py <year> <day> <problem_name>
```

**Examples:**
```bash
# Automatic - fetches "Red-Nosed Reports" and puzzle input automatically
python3 new_problem.py 2024 2

# Manual - specify the name yourself
python3 new_problem.py 2024 3 TobogganTrajectory
```

This will automatically:
- Fetch the problem name from Advent of Code
- Fetch your personalized puzzle input using your session cookie
- Create `{year}/{day}-{ProblemName}/` directory
- Create `solution.py` with the starter template
- Create `input.txt` with your puzzle input

### Setup

To enable automatic input fetching, ensure your Advent of Code session cookie is stored in `.env/session_cookie`.

### Workflow

1. Create a new problem directory: `python3 new_problem.py 2024 3`
2. Implement `part1()` and `part2()` in `solution.py`
3. Run your solution: `python3 solution.py`

That's it! No need to manually copy puzzle inputs.

## Years

- [2024](./2024/) - Previous year
- [2025](./2025/) - Current year
