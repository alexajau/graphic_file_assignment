import queue
from collections import deque
# bring in the file of names
file1 = open("names_list", "r")
names = [names.rstrip('\n') for names in file1]

premium = []
standard = []
economy = []

# put the names of the people into the correct queue
for word in names[:]:
    if word.startswith("P"):
        premium.append(word)
    elif word.startswith("S"):
        standard.append(word)
    elif word.startswith("E"):
        economy.append(word)

print("premium:", premium)
print("standard:", standard)
print("economy:", economy)


print("Weighted fair queuing: ")
for i in economy[:]:
    for i in range(3):
        if len(premium) > 0:
            print(premium.pop(0))
        else:
            pass
    for i in range(2):
        if len(standard) > 0:
            print(standard.pop(0))
        else:
            pass
    for i in range(1):
        if len(economy) > 0:
            print(economy.pop(0))
        else:
            pass
