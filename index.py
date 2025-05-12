def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
        
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        # Apply the discount if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

def main():
    # Get input from the user
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Validate inputs
        if original_price < 0 or discount_percent < 0:
            print("Error: Price and discount percentage cannot be negative.")
            return
            
        # Calculate the final price using the calculate_discount function
        final_price = calculate_discount(original_price, discount_percent)
        
        # Display the results
        if final_price < original_price:
            discount_amount = original_price - final_price
            print(f"\nOriginal price: ${original_price:.2f}")
            print(f"Discount applied: {discount_percent:.1f}%")
            print(f"Discount amount: ${discount_amount:.2f}")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"\nOriginal price: ${original_price:.2f}")
            print(f"No discount applied (discount must be 20% or higher)")
            print(f"Final price: ${final_price:.2f}")
            
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

if __name__ == "__main__":
    main()
