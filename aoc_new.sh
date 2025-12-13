#!/bin/bash
# Advent of Code - New Problem Setup Script
# Usage: aoc [year] [day] [problem_name]

# Determine AoC root from script location when sourced
_AOC_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

aoc() {
    local aoc_root="$_AOC_ROOT"

    # If no arguments, just go to AoC root
    if [ $# -eq 0 ]; then
        cd "$aoc_root" || {
            echo "❌ Error: Could not change to AoC directory: $aoc_root"
            return 1
        }
        echo "📂 Now in: $(pwd)"
        return 0
    fi

    # Check if we have at least year and day
    if [ $# -lt 2 ]; then
        echo "Usage: aoc [year] [day] [problem_name]"
        echo "   or: aoc  (to go to AoC root directory)"
        echo ""
        echo "Examples:"
        echo "    aoc                           # Go to AoC root"
        echo "    aoc 2024 3                    # Automatically fetch problem name"
        echo "    aoc 2024 3 TobogganTrajectory # Manually specify problem name"
        return 1
    fi

    # Change to AoC root directory
    cd "$aoc_root" || {
        echo "❌ Error: Could not change to AoC directory: $aoc_root"
        return 1
    }

    # Run the new_problem.py script and capture output
    local output
    output=$(python3 new_problem.py "$@" 2>&1)
    local exit_code=$?

    # Display the output
    echo "$output"

    # If successful, extract and navigate to the created directory
    if [ $exit_code -eq 0 ]; then
        # Extract the directory path from the output
        local problem_dir
        problem_dir=$(echo "$output" | grep "Created directory:" | sed 's/.*Created directory: //' | head -1)

        if [ -n "$problem_dir" ] && [ -d "$problem_dir" ]; then
            cd "$problem_dir" || {
                echo "❌ Error: Could not change to problem directory: $problem_dir"
                return 1
            }
            echo ""
            echo "📂 Now in: $(pwd)"
        else
            echo "⚠️  Could not determine problem directory"
            return 1
        fi
    else
        return $exit_code
    fi
}

# If script is sourced, export the function
# If executed directly, run the function
if [ "${BASH_SOURCE[0]}" = "${0}" ]; then
    aoc "$@"
fi
