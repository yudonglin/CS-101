# Yudong Lin - 2/19/2021
total_float_numbers:int = 0
counter:float = 0.0

#with open("mbox-short.txt","r",encoding="utf-8") as f:
with open("mbox-short.txt","r") as f:
    line_index = 0
    for line in f.readlines():
        line_index += 1
        if line.startswith("X-DSPAM-Confidence:"):
            total_float_numbers += 1
            float_number_found:float = float(line[line.find(":")+1:])
            print("Find '{}' on line {}".format(float_number_found,line_index))
            counter += float_number_found

print(
    'Found {0} floating point values.\n'
    'Where "{1}" is the number of floating point values you found (the counter variable).'
    .format(total_float_numbers,counter)
)