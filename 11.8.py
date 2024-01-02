def has_lucky_number(nums):
    """
    Kiểm tra xem danh sách các số có chứa số may mắn hay không.
    
    Parameters:
    - nums: danh sách các số
    
    Returns:
    - True nếu danh sách có chứa số may mắn, False nếu ngược lại.
    """
    for num in nums:
        if num % 7 == 0:
            return True
    return False

# Ví dụ 
numbers = [2, 6, 7, 9]
result = has_lucky_number(numbers)

print("Danh sách các số:", numbers)
print("Có chứa số may mắn hay không:", result)
