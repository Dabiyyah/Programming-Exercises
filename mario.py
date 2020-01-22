n = int(input("Give me a number between 0 and 23, inclusive: "))
m = int(n - 1)
i = int(1)
j = int(m)

while (n < 0) or (n > 23):
    n = int(input("Give me a number between 0 and 23, inclusive: "))
while i < n:

    for i in range (0, i):
        print("#" * i)

    for j in range (0, j):
        print("a" * m)
        print(f"{j}")

    print("exit")
    i = int(i + 1)
    j = int(m - 1)
