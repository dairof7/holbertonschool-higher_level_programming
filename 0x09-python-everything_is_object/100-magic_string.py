def magic_string(x=[0]):
    x[0] = x[0] + 1
    return ((("Holberton" + ", ") * x[0])[:-2])

for i in range(10):
    print(magic_string())
