# Prime Number Checker

A Python script that checks if a given integer is prime using the trial division algorithm with robust input validation.

## Features

- **Efficient primality testing**: Uses trial division up to `math.isqrt(n)` for optimal performance
- **Robust input validation**: Handles negative numbers, zero, non-integers, and whitespace
- **Clean code**: Follows PEP 8 standards with comprehensive docstrings and type hints
- **Interactive**: User-friendly prompts with clear error messages

## Usage

### Running the script

```bash
python prime_checker.py
```

The script will prompt you to enter a positive integer:

```
Enter a positive integer: 17
17 is prime.
```

### Invalid input handling

The script gracefully handles various invalid inputs:

- Negative numbers: "Error: Please enter a positive integer (greater than 0)."
- Zero: "Error: Please enter a positive integer (greater than 0)."
- Non-integers: "Error: 'abc' is not a valid integer. Please try again."
- Floats: "Error: '3.14' is not a valid integer. Please try again."

## Implementation Details

### Algorithm

The `is_prime()` function implements the trial division algorithm:

1. **Edge cases**: Numbers less than 2 are not prime, 2 is prime
2. **Even numbers**: All even numbers except 2 are not prime (quick rejection)
3. **Trial division**: Test odd divisors from 3 to √n inclusive
   - Uses `math.isqrt(n)` for integer square root (more efficient than `math.sqrt()`)
   - Only tests odd divisors (even divisors already ruled out)

### Complexity

- **Time complexity**: O(√n)
- **Space complexity**: O(1)

## Architecture

```
prime-checker/
├── prime_checker.py    # Main script with core functionality
└── README.md          # This file
```

### Functions

| Function | Purpose | Parameters | Returns |
|----------|---------|------------|---------|
| `is_prime(n)` | Check primality using trial division | `n: int` | `bool` |
| `get_validated_input()` | Get and validate user input | None | `int` |
| `main()` | Program entry point | None | `None` |

## Testing

The script handles various edge cases:

| Input | Expected Output |
|-------|-----------------|
| -5 | "Error: Please enter a positive integer" |
| 0 | "Error: Please enter a positive integer" |
| 1 | "1 is not prime." |
| 2 | "2 is prime." |
| 4 | "4 is not prime." |
| 17 | "17 is prime." |
| "abc" | "Error: 'abc' is not a valid integer" |
| "  42  " | "42 is not prime." (whitespace trimmed) |

## Requirements

- Python 3.8+
- Standard library only (sys, math)

## License

This project is open source and available for educational purposes.