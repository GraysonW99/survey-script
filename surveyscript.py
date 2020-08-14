# ttweetcli.py
# Grayson Whiteley
import random

print("Please specify file containing list of potential recipients. Example: testList")
emailList = input()
file1 = open(emailList, 'r')
lines = file1.readlines()
print("Retrieved %s emails!"% len(lines))
print("Please specify how many recipients to be randomly selected. Example: 2")
numRecipients = int(input())
recipients = []
size = len(lines)
for i in range(numRecipients):
    index = random.randrange(size)
    recipients.append(lines[index].strip())
    lines[index] = lines[size - 1]
    size -= 1
print("Retrieved %s random recipients"% len(recipients))
