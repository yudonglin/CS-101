# Yudong Lin - 2/22/2021
import random

iteration:int = 0

while True:
    a_random_float:float = round(random.uniform(0,4),2)
    print(a_random_float)
    if a_random_float == 4:
        break
    else:
        iteration += 1

print("It took {} iterations to generate 4.00".format(iteration))

if iteration < 100:
    print("Lucky!")
elif iteration > 1000:
    print("Ok... not a lucky try, isn't it?")
