for i in range(0, 101):
    if i == 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("buzz")
    else:
        print(i)
