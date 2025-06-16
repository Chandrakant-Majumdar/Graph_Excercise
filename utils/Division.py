def division(nums: list):
    """Divides the first number in a list by the last of the number.

    Args:   
        nums (list): A list of numbers where the first number is the dividend and the rest are divisors.
    Returns:
        float: The result of the division.
    """
    return nums[0]/nums[len(nums)-1]