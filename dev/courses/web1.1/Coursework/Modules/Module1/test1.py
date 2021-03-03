# *args

def add_all_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total

answer = add_all_numbers(1, 2, 3, 4, 5)
print(answer)