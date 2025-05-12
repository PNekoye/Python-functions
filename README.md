# Python-functions
# Discount Calculator

A Python program that calculates the final price of an item after applying a discount, based on specific discount rules.

## Description

This program features a `calculate_discount` function that determines whether a discount should be applied to an item based on the discount percentage provided. The discount is only applied if it's 20% or higher; otherwise, the original price is returned.

## Features

- Calculates the final price after applying a discount
- Applies discounts only when they are 20% or higher
- Provides detailed output including original price, discount percentage, and final price
- Includes input validation for price and discount values
- Formats currency values to two decimal places for readability

## Requirements

- Python 3.x

## How to Use

1. Run the program:
   ```
   python discount_calculator.py
   ```

2. Follow the prompts:
   - Enter the original price of the item
   - Enter the discount percentage

3. View the results showing whether a discount was applied and the final price

## Function Documentation

### `calculate_discount(price, discount_percent)`

Calculates the final price after potentially applying a discount.

**Parameters:**
- `price` (float): The original price of the item
- `discount_percent` (float): The discount percentage to potentially apply

**Returns:**
- float: The final price after discount (if applicable)

**Behavior:**
- If discount_percent is 20 or higher: Applies the discount and returns the discounted price
- If discount_percent is less than 20: Returns the original price unchanged

## Example Usage

### Example 1: Discount Applied
```
Enter the original price of the item: $100
Enter the discount percentage: 25

Original price: $100.00
Discount applied: 25.0%
Discount amount: $25.00
Final price after discount: $75.00
```

### Example 2: No Discount Applied
```
Enter the original price of the item: $50
Enter the discount percentage: 15

Original price: $50.00
No discount applied (discount must be 20% or higher)
Final price: $50.00
```

## Error Handling

The program handles several types of errors:
- Non-numeric inputs: Prompts an error message asking for valid numbers
- Negative values: Prevents calculations with negative prices or discount percentages

## Future Improvements

Potential enhancements for this program:
- Add support for different discount thresholds
- Implement bulk discount calculations
- Create a graphical user interface (GUI)
- Add ability to calculate discounts for multiple items
- Save discount calculations to a file

## License

Feel free to use and modify this code for your own projects.

## Author

[Purity Nekoye]
