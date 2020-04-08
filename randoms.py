import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
print("""
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?

    Computer print the random numbers between 5 to 20, the smallest number is 5,
    the largest number is 20.



What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?

    Computer print the odd numbers between 3 to 10, the smallest number is 3,
    the largest number is 9.The line 2 can not produce 4.



What did you see on line 3?
What was the smallest number you could have seen, what was the largest?

    line 3 produce the random numbers between 2.5 to 5.5, the smallest number is 2.5,
    the largest number is 5.5.

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
""")
print(random.randint (1, 100))
