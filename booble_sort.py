elements = [7,3,1,2,5]

size = len(elements)

print(f"Before sorting {elements}")

for i in range(size):
    for j in range(size-i-1):
        if elements[j] > elements[j+1]:
            elements[j], elements[j+1]= elements[j+1], elements[j]
            print(elements)

print(f"After sorting {elements}")
print(elements[::-1])