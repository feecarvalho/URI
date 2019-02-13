x = int(input())
y = int(input())

if x < y:
    for num in range(x + 1, y):
        if (num % 5) == 3 or (num % 5) == 2:
            print(num)
elif y < x:
    for num in range(y + 1, x):
        if (num % 5) == 3 or (num % 5) == 2:
            print(num)
