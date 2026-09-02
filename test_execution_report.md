# Test Results — Inventory Management System

Ran with: `pytest tests/test_inventory.py -v`
Result: 25 passed, 0 failed, 0.09s

## All tests

| Test | Function | Result |
|---|---|---|
| test_add_item_success | add_items | Passed |
| test_add_item_duplicate_raises_error | add_items | Passed |
| test_add_item_negative_stock_raises_error | add_items | Passed |
| test_add_item_negative_price_raises_error | add_items | Passed |
| test_get_item_returns_none_when_not_found | get_item | Passed |
| test_get_item_by_name | get_item | Passed |
| test_add_stock_success | add_stock | Passed |
| test_add_stock_item_not_found_raises_error | add_stock | Passed |
| test_add_stock_zero_quantity_raises_error | add_stock | Passed |
| test_remove_stock_success | remove_stock | Passed |
| test_remove_stock_item_not_found_raises_error | remove_stock | Passed |
| test_remove_stock_more_than_available_raises_error | remove_stock | Passed |
| test_remove_stock_zero_quantity_raises_error | remove_stock | Passed |
| test_place_order_success | place_order | Passed |
| test_place_order_item_not_found_raises_error | place_order | Passed |
| test_place_order_zero_quantity_raises_error | place_order | Passed |
| test_place_order_insufficient_stock_raises_error | place_order | Passed |
| test_cancel_order_success | cancel_order | Passed |
| test_cancel_order_not_found_raises_error | cancel_order | Passed |
| test_get_low_stock_report | get_low_stock_report | Passed |
| test_get_low_stock_report_empty_when_all_fine | get_low_stock_report | Passed |
| test_get_most_ordered_items | get_most_ordered_items | Passed |
| test_get_most_ordered_items_empty_when_no_orders | get_most_ordered_items | Passed |
| test_get_all_items_returns_all | get_all_items | Passed |
| test_get_all_items_empty_db | get_all_items | Passed |

## Coverage by function

| Function | Tests |
|---|---|
| add_items | 4 |
| get_item | 2 |
| add_stock | 3 |
| remove_stock | 4 |
| place_order | 4 |
| cancel_order | 2 |
| get_low_stock_report | 2 |
| get_most_ordered_items | 2 |
| get_all_items | 2 |

## Raw output

```
tests/test_inventory.py::test_add_item_success PASSED                    [  4%]
tests/test_inventory.py::test_add_item_duplicate_raises_error PASSED     [  8%]
tests/test_inventory.py::test_add_item_negative_stock_raises_error PASSED [ 12%]
tests/test_inventory.py::test_add_item_negative_price_raises_error PASSED [ 16%]
tests/test_inventory.py::test_get_item_returns_none_when_not_found PASSED [ 20%]
tests/test_inventory.py::test_get_item_by_name PASSED                    [ 24%]
tests/test_inventory.py::test_add_stock_success PASSED                   [ 28%]
tests/test_inventory.py::test_add_stock_item_not_found_raises_error PASSED [ 32%]
tests/test_inventory.py::test_add_stock_zero_quantity_raises_error PASSED [ 36%]
tests/test_inventory.py::test_remove_stock_success PASSED                [ 40%]
tests/test_inventory.py::test_remove_stock_item_not_found_raises_error PASSED [ 44%]
tests/test_inventory.py::test_remove_stock_more_than_available_raises_error PASSED [ 48%]
tests/test_inventory.py::test_remove_stock_zero_quantity_raises_error PASSED [ 52%]
tests/test_inventory.py::test_place_order_success PASSED                 [ 56%]
tests/test_inventory.py::test_place_order_item_not_found_raises_error PASSED [ 60%]
tests/test_inventory.py::test_place_order_zero_quantity_raises_error PASSED [ 64%]
tests/test_inventory.py::test_place_order_insufficient_stock_raises_error PASSED [ 68%]
tests/test_inventory.py::test_cancel_order_success PASSED                [ 72%]
tests/test_inventory.py::test_cancel_order_not_found_raises_error PASSED [ 76%]
tests/test_inventory.py::test_get_low_stock_report PASSED                [ 80%]
tests/test_inventory.py::test_get_low_stock_report_empty_when_all_fine PASSED [ 84%]
tests/test_inventory.py::test_get_most_ordered_items PASSED              [ 88%]
tests/test_inventory.py::test_get_most_ordered_items_empty_when_no_orders PASSED [ 92%]
tests/test_inventory.py::test_get_all_items_returns_all PASSED           [ 96%]
tests/test_inventory.py::test_get_all_items_empty_db PASSED              [100%]

============================== 25 passed in 0.03s ==============================
```