def count_smaller_elements(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result


# Чтение ввода
input_nums = list(map(int, input().split()))
output = count_smaller_elements(input_nums)

# Вывод результата
print(*output)
