x = 0
y = 1

fib = 0


for i in range(1,4000000):
    f = x + y
    x = y
    y = f
    if f % 2 == 0 :
        fib += f

print(f)
