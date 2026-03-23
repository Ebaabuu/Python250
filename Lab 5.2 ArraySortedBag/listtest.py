list1 = [4, 7, 5, 3, 12, None]
#        0  1  2  3  4   5
size = 5

counter = 0
for i in range(size, -1, -1):
    list1[i] = list1[i - 1]
list1[0] = None

print(list1)

