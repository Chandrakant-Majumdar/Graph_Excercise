def division(nums: list):
    """Divides the first number in a list by the last of the number.

    Args:   
        nums (list): A list of numbers where the first number is the dividend and the rest are divisors.
    Returns:
        float: The result of the division.
    Raises:
        ZeroDivisionError: If the last number is zero.
    """
    if nums[-1] == 0:
        raise ZeroDivisionError("Cannot divide by zero (last number in list is zero).")
    return nums[0]/nums[-1]