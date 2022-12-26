numbers = [1, 2, 3, 4, 5]
numbers_sq = []
for num in numbers:
    new_number = num ** 2
    numbers_sq.append(new_number)

is_even = []
is_odd = []
is_factor_of_3 = []

for num in numbers_sq:
    if num % 3 == 0:
        is_factor_of_3.append(num)
    elif num % 2 == 0:
        is_even.append(num)
    else:
        is_odd.append(num)

print(is_odd)
print(is_even)
print(is_factor_of_3)

x = 10
i = 0
z = 12

while i < x:
    z = z * 2
    if z > 342900:
        break
    print(f"{z}\n{i}")
    i = i + .00000001

while i < x:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

