# Yudong Lin - 2/19/2021
total:float = 0.0
count:int = 0

while 1:
    number:any = input("Enter a number:")
    if number != "done":
        try:
            number:float = float(number)
            total += number
            count += 1
        except:
            print("Invalid input, input '{}' is not accaptable!".format(number))
    else:
        break

print(
    "Total: {0}\n"
    "Count: {1}\n"
    "Average: {2}"
    .format(total,count,total/count)
)