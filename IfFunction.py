# Yudong Lin - 2/22/2021

def computegrade(score:float) -> str:
    try:
        score = float(score)
    except:
        return "Bad score"
    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        else:
            return "F"
    else:
        return "Bad score"

"""
#Yudong is using this for testing
#Do not use it unless you know what you are doing
import random
for i in range(20):
    score_for_testing:float = random.randint(-10,110)/100
    print("---------------")
    print("score:",score_for_testing)
    print("grade:",computegrade(score_for_testing))
"""

#print the result
score:float = input("Enter a score between 0.0 and 1.0: ")
print(computegrade(score))
