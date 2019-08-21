x = 0
y = 1


for i in range(1,4000000):
    f = x + y
    x = y
    y = f
    print(f)
