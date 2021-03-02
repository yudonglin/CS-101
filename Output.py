# Yudong Lin - 2/22/2021
from os import path,remove

#define the path (as a constant, but python doesn't have the idea of constant)
OUTPUT_FILE_PATH:str = "emails_output.txt"

#check if emails_output.text exists, if yes, remove the old one
if path.exists(OUTPUT_FILE_PATH): remove(OUTPUT_FILE_PATH)

#variables that are used for counting
counter_com:int = 0
counter_edu:int = 0
counter_org:int = 0

#open files
f_in = open("mbox.txt","r")
f_out = open(OUTPUT_FILE_PATH,"w")

for line in f_in.readlines():
    if "@" in line:
        if line.find(".com") != -1:
            f_out.write(line)
            counter_com += 1
        elif line.find(".edu") != -1:
            f_out.write(line)
            counter_edu += 1
        elif line.find(".org") != -1:
            f_out.write(line)
            counter_org += 1
    else:
        continue

#close files
f_in.close()
f_out.close()

#print result
print(
    "Solution:\n"
    "ending in .com: {0}\n"
    "ending in .edu: {1}\n"
    "ending in .org: {2}"
    .format(
        counter_com,
        counter_edu,
        counter_org
    )
)
