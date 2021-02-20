# Yudong Lin - 2/19/2021
def computepay(hours:float,rate:float) -> float:
    if rate >= 0:
        if hours > 40:
            return rate*40.0+1.5*rate*(hours-40.0)
        elif hours >= 0:
            return hours*rate
        else:
            raise Exception("No No No I will not let you put negative hours!")
    else:
        raise Exception("You want your workers to pay you? How dare you!")

h:float = float(input("How many hours?: "))
r:float = float(input("What is your hourly rate?: "))

grosspay:float = computepay(h,r)

print("grosspay: {}".format(grosspay))