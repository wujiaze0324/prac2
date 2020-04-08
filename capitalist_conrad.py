import random

PRICE_INCREASE = 0.1 # 10%
PRICE_DECREASE = 0.05  # 5%
MAX_INCREASE = 0.175
MIN_DECREASE = 0.175
MIN_PRICE = 0.01
MAX_PRICE = 1000
INITIAL_PRICE = 10.0
DAY = 0
OUTPUT_FILE = "conrad.txt"
out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
print("Starting price:${:,.2f}".format(price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:

    price_change = 0

    k = random.randint(1, 2)
    c = 0.01 < price < 1 or 100 < price <= 1000
    a = 1 <= price <= 100
    
    if 1 <= price <= 100 and random.randint(1, 2) == 1:

        price_change = random.uniform(0, MAX_INCREASE)
    elif  1 <= price <= 100 and random.randint(1, 2) == 2:

        price_change = random.uniform(-MIN_DECREASE, 0)
    elif 0.01 < price < 1 or 100 < price <= 1000 and random.randint(1, 2) == 1:

        price_change = random.uniform(0, PRICE_INCREASE)
    elif 0.01 < price < 1 or 100 < price <= 1000 and random.randint(1, 2) == 2:

        price_change = random.uniform(-PRICE_DECREASE, 0)
    DAY += 1
    price *= (1 + price_change)
    print("On day", int(DAY),"price is $", "${:,.2f}".format(price), file=out_file)
out_file.close()
print("done")
