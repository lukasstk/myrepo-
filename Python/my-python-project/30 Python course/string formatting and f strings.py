template = """Hello there,
                {name} this is an amazing way to do
                subbing my cool items."""

print(template)
template.format(name="J")  # .format replaces any word in a string in the {}
print(template.format(name="J"))
"hello\nanother".replace("\n", "")

print("hello\nanother")
print("hello\nanother".replace("another", "another1"))  # .replace replaces any character in the string

print("hello \
abc")

print("http:\\\\thisisawesome")  # u need two \\ to escape the line break

pi = 3.145226
print("{:.2f}".format(pi))  # .format on int, {:f} turns the int to a float, add .2 tho short the float to 2 decimals

print(format(pi, ".2f"))  # does the same thing

