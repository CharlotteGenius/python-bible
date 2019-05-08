import random

health = 50   # initial value

difficulty = 3   # easy=1 normal=2 hard=3

potion_health = int(random.randint(25,50) / difficulty)
# here, int() is a casting function to force a variable an integer
print(potion_health)

health = health + potion_health
print(health)





