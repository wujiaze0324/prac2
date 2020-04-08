finished = False
result = 0
while not finished:
    try:
        num = int(input("num:"))
        finished = True

    except: ValueError
    print("Please enter a valid integer.")
print("Valid result is:", result)