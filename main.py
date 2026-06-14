def calculate_pi_to_5_digits():
    """
    Calculate pi to the 5th digit using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to calculate 5 digits accurately
    getcontext().prec = 50
    
    def arctan(x, num_terms=100):
        """Calculate arctan(x) using Taylor series"""
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    one = Decimal(1)
    five = Decimal(5)
    two_three_nine = Decimal(239)
    
    pi_over_4 = 4 * arctan(one / five) - arctan(one / two_three_nine)
    pi = 4 * pi_over_4
    
    return float(pi)


def main():
    print("Hello from claude-api!")
    pi_value = calculate_pi_to_5_digits()
    print(f"Pi to the 5th digit: {pi_value:.5f}")


if __name__ == "__main__":
    main()
