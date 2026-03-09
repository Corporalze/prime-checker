#!/usr/bin/env python3
"""
Test suite for prime_checker.py

Tests the is_prime() function with various edge cases and inputs.
"""

import unittest
import math
from prime_checker import is_prime


class TestPrimeChecker(unittest.TestCase):
    """Test cases for the prime checker functionality."""

    def test_negative_numbers(self):
        """Negative numbers should not be prime."""
        for n in [-1, -5, -100, -997]:
            with self.subTest(n=n):
                self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_zero_and_one(self):
        """0 and 1 are not prime numbers."""
        for n in [0, 1]:
            with self.subTest(n=n):
                self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_small_primes(self):
        """Test small prime numbers."""
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for n in primes:
            with self.subTest(n=n):
                self.assertTrue(is_prime(n), f"{n} should be prime")

    def test_small_composites(self):
        """Test small composite numbers."""
        composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25]
        for n in composites:
            with self.subTest(n=n):
                self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_even_numbers(self):
        """Even numbers greater than 2 should not be prime."""
        for n in [4, 6, 8, 10, 100, 1000]:
            with self.subTest(n=n):
                self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_large_primes(self):
        """Test some known large prime numbers."""
        large_primes = [
            997,            # Largest 3-digit prime
            7919,           # 1000th prime
            104729,         # 10000th prime
            1299709,        # 100000th prime
        ]
        for n in large_primes:
            with self.subTest(n=n):
                self.assertTrue(is_prime(n), f"{n} should be prime")

    def test_large_composites(self):
        """Test some large composite numbers."""
        large_composites = [
            1000,           # 10^3
            10000,          # 10^4
            999999,         # Just under a million
            1000000,        # One million
            999983 * 2,     # Product of large prime and 2
        ]
        for n in large_composites:
            with self.subTest(n=n):
                self.assertFalse(is_prime(n), f"{n} should not be prime")

    def test_squares_of_primes(self):
        """Squares of prime numbers are composite."""
        prime_squares = [4, 9, 25, 49, 121, 169, 289, 361]
        for n in prime_squares:
            with self.subTest(n=n):
                self.assertFalse(is_prime(n), f"{n} (square of prime) should not be prime")

    def test_edge_case_two(self):
        """2 is the only even prime number."""
        self.assertTrue(is_prime(2), "2 should be prime")

    def test_performance_with_large_number(self):
        """Test with a reasonably large number to ensure algorithm efficiency."""
        # A 6-digit number that's not too large but still tests performance
        # 999983 is a prime, 999984 is composite
        self.assertTrue(is_prime(999983), "999983 should be prime")
        self.assertFalse(is_prime(999984), "999984 should not be prime")

    def test_specific_composites(self):
        """Test specific composite numbers with known factors."""
        test_cases = [
            (15, False),  # 3 * 5
            (49, False),  # 7 * 7
            (91, False),  # 7 * 13
            (121, False), # 11 * 11
            (221, False), # 13 * 17
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(is_prime(n), expected, f"{n} should be {expected}")


class TestInputValidation(unittest.TestCase):
    """Test cases for input validation (these would test get_validated_input in integration)."""

    def test_type_hints(self):
        """Verify that the is_prime function has proper type hints."""
        import inspect
        sig = inspect.signature(is_prime)
        # Check parameter type
        self.assertEqual(sig.parameters['n'].annotation, int)
        # Check return type
        self.assertEqual(sig.return_annotation, bool)


if __name__ == "__main__":
    unittest.main(verbosity=2)