def multipilication(nums: list):
    """    Multiplies a list of numbers together.

    Args:                           
        nums (list): A list of numbers to be multiplied.
    Returns:
        int: The product of the numbers in the list.
    """
    result = 1
    for num in nums:
        result *=num
    return result
