def line_config(a,b):
    def line_value(x):
        return a*x + b
    return line_value

line1 = line_config(3,4)
line2 = line_config(4,5)
print(line1(10))
print(line2(10))

