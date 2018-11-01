import statistics

example_list = [4,2,3,4,5,6,6,3,3,2,3,5,5,3,3]

x = statistics.mean(example_list)
y = statistics.median(example_list)
z = statistics.mode(example_list)
a = statistics.stdev(example_list)
b = statistics.variance(example_list)

print(x)
print(y)
print(z)
print(a)
print(b)
