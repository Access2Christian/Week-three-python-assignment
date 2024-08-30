def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or more, the discount is applied.
    Otherwise, the original price is returned.
    
    :param price: Original price of the item (float)
    :param discount_percent: Discount percentage to apply (float)
    :return: Final price after discount (float)
    """
    # Ensure the discount percent is within a valid range (0 to 100)
    if 0 <= discount_percent <= 100:
        if discount_percent >= 20:
            # Apply the discount
            discounted_price = price * (1 - discount_percent / 100)
            return round(discounted_price, 2)  # Round to 2 decimal places for currency format
        else:
            # No discount applied
            return round(price, 2)
    else:
        # Invalid discount percentage
        raise ValueError("Discount percentage must be between 0 and 100.")

# Function to handle user input and display results
def main():
    try:
        # Get user input for price and discount
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))

        # Calculate the final price using the calculate_discount function
        final_price = calculate_discount(original_price, discount_percentage)

        # Display the final price
        if final_price == original_price:
            print(f"No discount applied. The original price is: ${final_price:.2f}")
        else:
            print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
