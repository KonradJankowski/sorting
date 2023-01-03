# Program searches for a number from the list

list = [1, 4, 5, 9, 12, 18, 20, 21, 27, 32, 35, 48, 49, 51,54]
x = 12

start = 0
end = len(list) -1
find = False

while find == False:
    average = int((start + end) / 2)
    print(f"Aktualnie srawdzana liczba to: {list[average]}")
    if list[average] == x:
        find = True
        print(f"Poszukiwana liczba to {list[average]}")
    else:
        if list[average] >= x:
            end = average - 1
        else:
            start = average + 1
