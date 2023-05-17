import math
from statistics import mean, median, mode


list_str = input("Enter the numbers and seperate them with a comma: ")
list_comma = (list_str.split(","))
print(list_comma)

# Change to numbers
list = []
for luku in list_comma:
    list.append(float(luku))

# Tulostetaan min ja max
maxium = max(list)
minium = min(list)
meean = mean(list)
meedian = median(list)
moode = mode(list)

print(f'Max {maxium}\nMin {minium}\nMean {meean}\nMedian {meedian}\nMode {moode}')