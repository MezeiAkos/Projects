import random

n = int(input("Number of coin flips: "))
n0 = n
heads, tails = 0, 0
while n > 0:
    if random.randint(0, 1) == 0:
        heads += 1
    else:
        tails += 1
    n -= 1

heads_percentage = (heads / n0) * 100
tails_percentage = (tails / n0) * 100
print(f"{heads} heads, {tails} tails out of {n0} flips, {heads_percentage:.2f}% were heads, {tails_percentage:.2f}% "
      f"were tails")
