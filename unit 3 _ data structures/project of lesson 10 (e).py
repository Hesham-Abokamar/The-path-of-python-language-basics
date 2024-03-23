numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

grouped_numbers = []

size = 3

grouped_numbers = [numbers[i:i+size] for i in range(0, len(numbers), size)]

print(grouped_numbers)