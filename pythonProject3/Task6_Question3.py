num_list = [10, 501, 22, 37, 100, 999, 87, 351]
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1

happy_numbers = [num for num in num_list if is_happy(num)]

print("Actual List:", num_list)
print("Happy Numbers List:", happy_numbers)

