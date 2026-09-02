# Test Report — Inventory Management System

## What this project is
A command-line inventory and order management system built in Python with SQLite. It handles adding items, updating stock, placing and cancelling orders, and generating basic reports (low stock, most ordered items).

## What I tested
I wrote 25 automated tests using pytest, covering every function in the system: adding items, adding/removing stock, placing and cancelling orders, and the two reporting functions. Each function is tested for normal use, invalid input, and edge cases like zero quantity or empty results.

## Results
All 25 tests passed. No failures.

Breakdown:
- 11 tests check normal, expected behavior
- 10 tests check that invalid input is correctly rejected (negative numbers, duplicate items, missing items, insufficient stock)
- 4 tests check edge cases (empty database, zero quantity)

## Regression check (before/after comparison)
To confirm the tests actually catch real bugs, I made one deliberate change to the code and re-ran the tests.

**Change:** In `remove_stock`, I changed the stock check from `stock > item["stock"]` to `stock >= item["stock"]`.

**Result:** 1 test failed. The edge case of removing exactly the full remaining stock now failed, because `>=` incorrectly treated "removing everything" the same as "removing too much."

**Fix:** Reverted the change back to `>`. All 25 tests passed again.

This confirmed the test suite catches real, meaningful bugs, not just passing by default.

## What I'd flag going forward
Small changes to comparison operators (`>` vs `>=`) are an easy way to introduce bugs, especially around boundary values like "exactly the remaining stock." Any future changes to this kind of logic should be run against the full test suite before merging.