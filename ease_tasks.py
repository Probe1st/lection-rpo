# сумма цифр числа
def sum_digits_of_number(number: int):
    sum_digits = 0
    # "1331"
    number_str = str(number)

    for digit in number_str:
        # "1" "3" "3" "1"
        sum_digits += int(digit)

    return sum_digits
    # print(sum_digits_of_number(1331))

# количество гласных
def count_vowels(string):
    vowels = "euoiay"
    count = 0

    for symbol in string:
        if symbol in vowels:
            count += 1

    return count

    # print(count_vowels("asdohe"))

# минимум/максимум в последовательности
def min_max(nums):
    max_num = nums[0]
    min_num = nums[0]

    for num in nums:
        if num > max_num:
            max_num = num

        if num < min_num:
            min_num = num

    return max_num, min_num

    # print(type(min_max([2, 3, 1])))

# строго возрастающая последовательность

# делители числа

