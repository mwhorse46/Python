x = 6

def example():
    global x
    print(x)
    x+=5
    print(x)
example()

def example2():
    globx = x
    print(globx)
    globx += 5
    print(globx)
    return globx
x = example2()
print(x)
