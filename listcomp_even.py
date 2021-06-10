# create a list comprehension that only includes even numbers

a = [n * n for n in range(0,11)]

b = [n for n in a if n % 2 == 0]

print("a is ", a)
print("b is ", b)
