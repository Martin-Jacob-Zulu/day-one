# Easiest way to create an empty list and/or list
list1 = range(0, 99)
sum = 0
average = 0
over_average = 0
list2 = []
list3 = []
for i in list1:
    sum += i
average = sum / len(list1)
for x in list1:
    if x > average:
        list2.append(x)
        over_average += 1
    else:
        list3.append(x)

list4 = list3 + list2
list4.pop(1)
# list2.remove(50)
list2.reverse()
list2.sort()
print(list2.count(56))

# list2_extended = 4 * list2

print(f"Sum : {sum} \nAverage : {average} \nOver Averahe : {over_average} "
      f"\nList 2  : {list2}")
print(list2[20 : 35])

# Sorting Done
# Append Done
# Reverse Done
# Pop Done
# Remove Done
# Count Done
# Extend Done
# Index Done
# Insert Done
