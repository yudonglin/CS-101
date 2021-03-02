# Yudong Lin - 2/22/2021
line_match:int = 0
emails_list:list = []

with open("mbox-short.txt","r") as f:
    for line in f.readlines():
        if line.startswith("From "):
            char_list:list = line.split()
            email_address_found = char_list[1]
            print(email_address_found)
            line_match +=1
            #if the email addres is unique, then add it to the list
            if email_address_found not in emails_list:
                emails_list.append(email_address_found)

print("Found {} solutions".format(line_match))
print("And there are {} unique results".format(len(emails_list)))
