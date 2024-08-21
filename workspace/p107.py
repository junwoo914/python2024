import random
def rolling_dice(pip,reapt):
    for r in range(1,reapt+1):
        n=random.randint(1,pip)
        print(n)
rolling_dice(6,5)
