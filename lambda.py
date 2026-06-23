number = list(range(1,11))
even_numbers = list(filter(lambda x: x % 2 == 0, number))
print(even_numbers)

odd = list(range(1,11))
odd_number = list(filter(lambda x: x % 2 != 0, odd))
print(odd_number)
#Other use case using lambda
numbers = list(range(1,11))
tripled_numbers = list(map(lambda x: x * 3, numbers))
print(tripled_numbers)

