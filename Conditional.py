# Yudong Lin - 2/19/2021

score:float = float(input("Enter a score between 0.0 and 1.0:"))

#score = 0.65 #This is what only Yudong can use to test, don use it

grade_letters:tuple = ("A","B","C","D","F")

if 0.0 <= score <= 1.0:
    if score >= 0.9:
        print(grade_letters[0])
    elif score >= 0.8:
        print(grade_letters[1])
    elif score >= 0.7:
        print(grade_letters[2])
    elif score >= 0.6:
        print(grade_letters[3])
    else:
        print(grade_letters[4])
else:
    print("Error, the range has to be between 0.0 and 1.0")
    #raise Exception("Hey, the range needs to be between 0.0 and 1.0！")
